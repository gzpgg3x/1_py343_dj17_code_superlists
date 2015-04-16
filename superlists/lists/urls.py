# from django.conf.urls import patterns, url
# # from django.contrib import admin

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'superlists.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     # url(r'^admin/', include(admin.site.urls)),
#     # url(r'^superlists/$', superlists.views.home, name="home"),
#     # url(r'^$', 'lists.views.home_page', name="home"),
#     # # url(r'^/lists/$', include(lists.views,site)),
#     # url(r'^lists/', include('lists.urls')),    
#     # # url(r'^$lists/(+1)/', 'lists.views.view_list', name=''),
#     # # url(r'^lists/(.+)/$', 'lists.views.view_list', name='view_list'),
#     url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),   
#     url(r'^(\d+)/add_item$', 'lists.views.add_item', name='add_item'), 
#     # # url(r'^lists/the-only-list-in-the-world/$', 'lists.views.view_list', name='view_list'),
#     # # url(r'^new/$', 'lists.views.new', name='new'),
#     url(r'^new$', 'lists.views.new_list', name='new_list'),
# )


from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
)
