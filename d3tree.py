
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404

from tractatusapp.models import *

import os 
from settings import printdebug




#  EXAMPLE OF APIs
# 
# >>> top_units = TextUnit.objects.filter(level=0)
# >>> top_units
# [<TextUnit: 1>, <TextUnit: 2>, <TextUnit: 3>, <TextUnit: 4>, <TextUnit: 5>, <TextUnit: 6>, <TextUnit: 7>]
# >>> one = top_units[0]
# >>> one.hascontents.all()
# [<TextFragment: [527] <div class="ogd">The world is everything...>, <TextFragment: [1053] <div class="pmc">The world is all that i...>, <TextFragment: [1579] <div class="ger">Die Welt ist alles, was...>]
# >>> text1 = _[0]
# >>> text1.language
# <Language: english>
# >>> text1.in_expression.all()
# [<TextExpression: [3] text_ogden.html>]





# using a static json dump of the Tractatus
# create it here: tractatus/getjson/
								
								
def index(request):
	# all_units = TextUnit.objects.all()
	filename = "data"
	return render_to_response('tractatusapp/d3tree/d3tree.html', 
							{ 
								'filename' : filename
							},
							  context_instance=RequestContext(request))





# TODO: this is just a stub from other views 

# def get_sentence(request, num=None, version=None):
# 	DEFAULT_VERSION = "ogden"  # available versions: 'ogden' , 'pears', 'german' 
# 	if not num:
# 		num = 1
# 	if not version:
# 		return redirect("/tractatus/sentence/%s/%s/" % (num, DEFAULT_VERSION))
#   
# 	unit = TextUnit.objects.get(name=num)
# 	next = unit.tractatus_next()
# 	prev = unit.tractatus_prev()
# 	text = ""
# 	if version == 'ogden':
# 		text = unit.textOgden()
# 	if version == 'pears':
# 		text = unit.textPears()
# 	if version == 'german':
# 		text = unit.textGerman()
# 	
# 	return render_to_response('onesentence/sentence.html', 
# 							{ 
# 								'unit' : unit,
# 								'next' : next,
# 								'prev' : prev,
# 								'text' : text, 
# 								'currentversion' : version,
# 							},
# 							  context_instance=RequestContext(request))
# 
# 
# 



