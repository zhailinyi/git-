from django.conf.urls.defaults import patterns, url
from django.contrib.admin.views.decorators import staff_member_required

from oscar.core.application import Application
from oscar.apps.dashboard.offers import views
from oscar.apps.dashboard.nav import register, Node

node = Node('Offers')
node.add_child(Node('All offers', 'dashboard:offer-list'))
register(node, 7)


class OffersDashboardApplication(Application):
    name = None
    list_view = views.OfferListView
    metadata_view = views.OfferMetaDataView
    condition_view = views.OfferConditionView
    benefit_view = views.OfferBenefitView
    preview_view = views.OfferPreviewView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.list_view.as_view(), name='offer-list'),
            # Creation
            url(r'^metadata/$', self.metadata_view.as_view(), name='offer-metadata'),
            url(r'^condition/$', self.condition_view.as_view(), name='offer-condition'),
            url(r'^benefit/$', self.benefit_view.as_view(), name='offer-benefit'),
            url(r'^preview/$', self.preview_view.as_view(), name='offer-preview'),
            # Update
            url(r'^(?P<pk>\d+)/metadata/$', self.metadata_view.as_view(update=True), name='offer-metadata'),
            url(r'^(?P<pk>\d+)/condition/$', self.condition_view.as_view(update=True), name='offer-condition'),
            url(r'^(?P<pk>\d+)/benefit/$', self.benefit_view.as_view(update=True), name='offer-benefit'),
            url(r'^(?P<pk>\d+)/preview/$', self.preview_view.as_view(update=True), name='offer-preview'),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = OffersDashboardApplication()
