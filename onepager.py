
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





def index(request):

	version = request.GET.get("version", None)
	DEFAULT_VERSION = "ogden"
	ALLOWED_VERSIONS = ["ogden", "pears", "german"]
	if not version or version not in ALLOWED_VERSIONS:
		version = DEFAULT_VERSION

	all_units = TextUnit.objects.all()
	return render_to_response('tractatusapp/onepager/index.html',
							{
								'all_units' : all_units,
								'currentversion' : version,
							},
							  context_instance=RequestContext(request))
