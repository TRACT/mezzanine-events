from tastypie.resources import ModelResource
from mezzanine_events.models import Event

class EventsResource(ModelResource):
	class Meta:
		queryset = Event.objects.all()
		#allowed_methods = ['get']