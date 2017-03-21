
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404

from tractatusapp.models import *

import os
from settings import printdebug


import json


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
#
# >>> TextFragment.objects.filter(textunit=one)
# [<TextFragment: [527] <div class="ogd">The world is everything...>, <TextFragment: [1053] <div class="pmc">The world is all that i...>, <TextFragment: [1579] <div class="ger">Die Welt ist alles, was...>]




def index(request):
	a_level = request.GET.get()
	top_units = TextUnit.objects.filter(level__in=[0])

	return render_to_response('tractatusapp/wholetext/test.html',
							{
								'units' : top_units
							},
							  context_instance=RequestContext(request))





def wholetext(request):
	a_level = request.GET.get('level', 'all')
	a_fontsize = request.GET.get('fontsize', '14')
	if a_level in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
		units = TextUnit.objects.filter(level=int(a_level))
	else:
		units = TextUnit.objects.all()

	return render_to_response('tractatusapp/wholetext/wholetext.html',
							{
								'units' : units,
								'fontsize' : a_fontsize,
							},
							  context_instance=RequestContext(request))





def getjson(request):
	"""
	View used for outputting JSON for internal purposes
	"""

	tree = [buildJson(el) for el in TextUnit.objects.filter(level__in=[0])]
	temp = {'name' : 'TLP', 'children' : tree}
	text = json.dumps(temp)

	return render_to_response('tractatusapp/wholetext/jsontext.html', 
							{
								'text' : text
							},
							  context_instance=RequestContext(request))



def buildJson(el):
	new = {}
	CHILDREN = el.get_children()
	new['name'] = el.name
	new['size'] = len(CHILDREN) or 1
	if CHILDREN:
		new['children'] = [buildJson(x) for x in CHILDREN]
	return new


  # new_json_data.write(json.dumps(build_JIT_dict(data)))
#
# def build_D3S_dict(old, level=0):
#   """
#   For d3s examples all we need is a json with name, children and size .. eg
#
#   {
#  "name": "flare",
#  "children": [
#   {
#    "name": "analytics",
#    "children": [
# 	{
# 	 "name": "cluster",
# 	 "children": [
# 	  {"name": "AgglomerativeCluster", "size": 3938},
# 	  {"name": "CommunityStructure", "size": 3812},
# 	  {"name": "HierarchicalCluster", "size": 6714},
# 	  {"name": "MergeEdge", "size": 743}
# 	 ]
# 	},
# 	etc...
#   """
#   new = {}
#   thisChildren = old.get("children", [])
#   new['name'] = old['name'] or old['data']
#   new['size'] = len(thisChildren) or 1
#   if thisChildren and level < DEPTH_LEVEL:
# 	new['children'] = [build_D3S_dict(x, level+1) for x in thisChildren]
#   else:
# 	# new['children'] = []	# if left empty, D3 gets confused.
# 	pass
#   return new
#
#
#
#
