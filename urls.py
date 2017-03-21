from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',

    # WHOLE TEXT
    # just for testing, not very useful...
    # =========
    url(r'^wholetext$', 'tractatusapp.wholetext.wholetext', name='wholetext'),
    url(r'^getjson', 'tractatusapp.wholetext.getjson', name='getjson' ),



    # ONE-PAGER
    # =========
    url(r'^tractatus/onepage$', 'tractatusapp.onepager.index', name='indexmanysentences'),
    # ===== for backward compatibility:
    url(r'^manysentences$', 'tractatusapp.onepager.index'),
    # ===== end


    # TYPEWRITER APP
    # =========
    url(r'^typewriter$', 'tractatusapp.typewriter.index', name='indexsentence'),
    url(r'^typewriter/(?P<num>.+)/(?P<version>\w+)/$', 'tractatusapp.typewriter.get_sentence', name='get_sentence_version'),
    url(r'^typewriter/(?P<num>.+)/$', 'tractatusapp.typewriter.get_sentence', name='get_sentence'),
    # ===== for backward compatibility:
    url(r'^onesentence$', 'tractatusapp.typewriter.index', ),
    url(r'^onesentence/(?P<num>.+)/(?P<version>\w+)/$', 'tractatusapp.typewriter.get_sentence'),
    url(r'^onesentence/(?P<num>.+)/$', 'tractatusapp.typewriter.get_sentence'),
    # ===== end



    # SPACETREE
    # =========
    url(r'^spacetree$', 'tractatusapp.spacetree.spacetree', name='spacetree'),



    # D3 VIEWS
    # =========
    url(r'^d3tree$', 'tractatusapp.d3tree.index', name='d3index'),


    #finally
    # =========
    url(r'^$',
    direct_to_template, {
       'template': 'tractatusapp/home.html' ,
       }, name='witt_about'
    ),

    )
