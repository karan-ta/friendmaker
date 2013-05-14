# Create your views here.
import urllib
import urllib2
import urlparse

from django.shortcuts import render_to_response
from django.template import RequestContext

FB_APP_ID = '387128734733148'
FB_APP_SECRET = '6d63baf6f9fe680a204b9bb2f1c9eaf0'
FB_RETURN_URL = 'http://127.0.0.1:8000/comeback'

def home(request):

    args = dict(client_id=FB_APP_ID, redirect_uri=FB_RETURN_URL, scope='user_about_me,user_activities,user_birthday,user_checkins,user_education_history,user_events,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_online_presence,user_photo_video_tags,user_photos,user_relationships,user_relationship_details,user_religion_politics,user_status,user_videos,user_website,user_work_history,email,read_friendlists,read_insights,read_mailbox,read_requests,read_stream,xmpp_login,ads_management,create_event,manage_friendlists,manage_notifications,offline_access,publish_checkins,publish_stream,rsvp_event,sms,publish_actions,manage_pages')
    fburl = "https://graph.facebook.com/oauth/authorize?" + urllib.urlencode(args)
    return render_to_response('home.html',
                              {
                               'fburl': fburl},
                              context_instance=RequestContext(request))


def comeback(request):
    if request.method != 'GET' or 'code' not in request.GET:
        assert False, 'wrong!'

    code = request.GET["code"]
    token_url = "https://graph.facebook.com/oauth/access_token?client_id=%s&type=web_server&redirect_uri=%s&client_secret=%s&code=%s"
    token_url = token_url % (FB_APP_ID, urllib.quote_plus(FB_RETURN_URL), FB_APP_SECRET, code)        
    t = urllib2.urlopen(token_url)
    resp = urlparse.parse_qs(t.read())
    oauth_access_token = resp["access_token"][0]
    
    myself_url = "https://graph.facebook.com/me?%s" % urllib.urlencode(dict(access_token=oauth_access_token))

    myFriend_url = "https://graph.facebook.com/me/friends?%s" % urllib.urlencode(dict(access_token=oauth_access_token))

    myProfileFeed_url = "https://graph.facebook.com/me/feed?%s" % urllib.urlencode(dict(access_token=oauth_access_token))

    myLikes_url = "https://graph.facebook.com/me/likes?%s" % urllib.urlencode(dict(access_token=oauth_access_token))

    myPhotoAlbum = "https://graph.facebook.com/me/albums?%s" % urllib.urlencode(dict(access_token=oauth_access_token))

    myMovies = "https://graph.facebook.com/me/movies?%s" % urllib.urlencode(dict(access_token=oauth_access_token))

    myBooks = "https://graph.facebook.com/me/books?%s" % urllib.urlencode(dict(access_token=oauth_access_token))

    myMusic = "https://graph.facebook.com/me/music?%s" % urllib.urlencode(dict(access_token=oauth_access_token))

    mf = urllib2.urlopen(myFriend_url)
    return HttpResponse(str(m.read()))

