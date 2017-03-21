
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse

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


#
# idea: one sentence per screen (with versions selctions buttons)
# THe urls need to contain the sentence number so we always know where we are
#	- from a number we can calculate the 'next' sentence




def index(request):
	all_units = TextUnit.objects.all()
	return render_to_response('tractatusapp/typewriter/index.html',
							{
								'all_units' : all_units
							},
							  context_instance=RequestContext(request))




def get_sentence(request, num=None, version=None):
	DEFAULT_VERSION = "ogden"  # available versions: 'ogden' , 'pears', 'german'
	if not num:
		num = 1
	if not version:
		return HttpResponseRedirect(reverse('get_sentence_version' , args=(num, DEFAULT_VERSION)))

		# return redirect("/tractatus/sentence/%s/%s/" % (num, DEFAULT_VERSION))

  	try:
		unit = TextUnit.objects.get(name=num)
		next = unit.tractatus_next()
		prev = unit.tractatus_prev()
		text = ""
		if version == 'ogden':
			text = unit.textOgden()
		if version == 'pears':
			text = unit.textPears()
		if version == 'german':
			text = unit.textGerman()
	except:
		# 2016-11-04
		raise Http404

	return render_to_response('tractatusapp/typewriter/sentence.html', 
							{
								'unit' : unit,
								'next' : next,
								'prev' : prev,
								'text' : text,
								'currentversion' : version,
							},
							  context_instance=RequestContext(request))
