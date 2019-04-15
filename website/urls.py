"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

from rest_framework_jwt.views import obtain_jwt_token

from apps.article.views import ArticleCreated
from apps.course.views import CoursesList, CourseCreatedList, CourseListCreated, MeCoursesList
from apps.forum.views import Forum_plateView, ForumView, CommentView, Parent_CommentView
from apps.support.views import LinkList, EmailsList, BannerList
from apps.user.views import test, captcha_refresh, yan, login_view, UserGetInfo, UserGetAllInfo, \
    PersonOthers, Register, active_user, get_message, UserMessages, qq, getClback, getClbackQQ
from django.views.generic import TemplateView

from website import settings
from apps.article import views
from apps.user.views import logout_view, Person, PersonApi,to_login
from rest_framework import routers

router = routers.DefaultRouter()
router.register('article_list', views.ArticleListView)
router.register('me_article_list', views.MeArticleListView)
router.register('ArticleCommit', views.ArticleCommit)
router.register('follow_list', views.FollowListView)
router.register('category', views.CategoryView)
router.register('article_Comment', views.ArticleCommintView)
router.register('comment_reply', views.ArticleCommentReplyView)
router.register('PersonApi', PersonApi)
router.register('info', UserGetInfo)
router.register('all_info', UserGetAllInfo)
# router.register('user_disbale', UserDisbale)
router.register('PersonOthers', PersonOthers)
router.register('UserMessages', UserMessages, base_name='UserMessages')
router.register('article', ArticleCreated)
router.register('courseList', CoursesList)
router.register('mecourseList', MeCoursesList)
router.register('course', CourseCreatedList)
router.register('Addtutorial', CourseListCreated)
router.register('BannerList', BannerList)
router.register('EmailsList', EmailsList)
router.register('LinkList', LinkList)
router.register('forum/category', Forum_plateView)
router.register('forum', ForumView)
router.register('CommentView', CommentView)
router.register('Parent_CommentView', Parent_CommentView)

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('',test), # 这是生成验证码的图片
    url(r'^captcha/', include('captcha.urls')),
    path('refresh/', captcha_refresh),  # 这是生成验证码的图片
    path('yan/', yan),  # 这是生成验证码的图片
    path('', views.Article_list, name='home'),
    path('login/', login_view, name='index'),
    path('info/', get_message, name='info'),
    path('person/', include('apps.user.urls')),
    path('logou/', logout_view, name='logou'),
    path('register/', Register.as_view(), name='register'),
    path('article/', include('apps.article.urls')),
    path('course/', include('apps.course.urls')),
    path('support/', include('apps.support.urls')),
    path('forum/', include('apps.forum.urls')),
    url(r'^activate/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', active_user, name='active_user'),
    url(r'^search/', include('haystack.urls'), name='haystack_search'),

    re_path(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("api-docs/", include_docs_urls("API文档")),
    re_path(r'api/login/$', obtain_jwt_token),  # jwt认证
    url('auth-qq', to_login, name='qq-login'),
    url('qq', qq, name='qq'),
    url('callbackget', getClback, name='callbackget'),
    url('getClbackQQ', getClbackQQ, name='getClbackQQ'),
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATI_ROOT})  # 配置文件上传html显示
]
