from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Control, Implementation
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from functools import lru_cache
import re
from .forms import *

#@lru_cache(maxsize=128)
def get_all_controls():
    all_controls = list(Control.objects.all())
    control_name_plus_text = []
    control_text = {}
    control_guidance = {}
    for control in all_controls:
        control_text[control.number] = control.control_text
        control_name_plus_text.append(control.number + ": " + control.control_text)
        control_guidance[control.number] = control.supplemental_guidance
    return control_name_plus_text, control_text, control_guidance

def highlight_matches(query, text):
    def span_matches(match):
        html = '<span class="query">{0}</span>'
        return html.format(match.group(0))
    return re.sub(query, span_matches, text, flags=re.I)

def index(request):
    args = {}
    return render(request, 'search_box.html', args)	

def search(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    all_controls, control_dict, control_guidance = get_all_controls()
    print(search_text)	
    search_results = process.extract(search_text, all_controls, limit=10, scorer=fuzz.partial_ratio)
#	print(search_results)	
    results = []
    counter = 0
    for result in search_results:
#		print(result[0].split(':')[0])
        temp_result = []
        control=result[0].split(':')[0]
#		print(control_dict[control])
        temp_result.append(counter)
        counter += 1
        temp_result.append(control)
        if len(search_text) > 2:		
            control_text = highlight_matches(search_text, control_dict[control])
        else:
            control_text = control_dict[control]
        temp_result.append(control_text)
        temp_result.append(control_guidance[control])
        results.append(temp_result)

    return render_to_response('ajax_search.html', {'controls': results})

def implementations(request):
    all_implementations = list(Implementation.objects.all())
    
    return render(request, 'implementations.html', {'implementations': all_implementations})

def add_implementation(request):
    if request.method == "POST":
        form = AddImplementationForm(request.POST)
        # if form.is_valid():
    else:
        form = AddImplementationForm()
    return render(request, 'add-implementation.html', {'form': form})

