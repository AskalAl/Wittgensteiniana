
from django import template 
from tractatus.tractatusapp import models

register = template.Library() 

#
## for People template
#
#@register.inclusion_tag('admin/snippets/personfactoid_info.html') 
#def display_personfactoids(person_id): 
#    person = models.Person.objects.get(id__exact=person_id) 
#    # factoids = models.Factoids.objects.filter(people=person)
#    return { 'person': person }
#
#@register.inclusion_tag('admin/snippets/personwitnessfactoid_info.html') 
#def display_personwitness(person_id): 
#    person = models.Person.objects.get(id__exact=person_id) 
#    # factoids = models.Factoids.objects.filter(people=person)
#    return { 'person': person }
#
#@register.inclusion_tag('admin/snippets/personproanimafactoid_info.html') 
#def display_personproanima(person_id): 
#    person = models.Person.objects.get(id__exact=person_id) 
#    # factoids = models.Factoids.objects.filter(people=person)
#    return { 'person': person }
#
#
#
#
## for Document template
#
#
#@register.inclusion_tag('admin/snippets/charterfactoids_info.html') 
#def display_charterfactoids(document_id): 
#    document = models.Source.objects.get(id__exact=document_id) 
#    return { 'document': document }
