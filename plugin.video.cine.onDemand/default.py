# -*- coding: utf-8 -*-

import base64
import cookielib,sys
import urllib2,urllib,re,os

from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
import xbmcplugin,xbmcgui,xbmc,xbmcaddon

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
Addon = xbmcaddon.Addon('plugin.video.series.onDemand')
profile = xbmc.translatePath(Addon.getAddonInfo('profile'))
addonsettings = xbmcaddon.Addon(id='plugin.video.series.onDemand')

__language__ = addonsettings.getLocalizedString
home = addonsettings.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

def main():
    lista=[]
    std_url = "http://iptvbrasil.tk"
    file = "vod.xml"
    link=get_url(std_url,file)

    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    if len(soup('channels')) > 0 :
        channels = soup('channel')
        for channel in channels:
            videoTitle = channel('name')[0].string
            lista.append(videoTitle)

        if xbmcPlayer.isPlaying():
                xbmcPlayer.stop()
        playList.clear()    
        
        dialog = xbmcgui.Dialog()
        ret = dialog.select(__language__(30008),lista)
        for i, name in enumerate(lista):
            if ret == i:
                channel = soup.find('channel', attrs={'name' : lista[i]})

                items = channel.findAll("item")
                for item in items:
                    try:
                        videoTitle=item.title.string
                    except:
                        pass
                    try:
                        url=item.link.string
                        
                    except:
                        pass
                    try:
                        thumbnail=item.thumbnail.string
                        
                    except:
                        thumbnail=""
                    #print videoTitle,url,thumbnail

                    listitem = xbmcgui.ListItem(videoTitle, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
                    listitem.setInfo('video', {'videoTitle': videoTitle } )
                    playList.add(url,listitem=listitem)
                    addLink(videoTitle,url,thumbnail)
        
            else:
                print ("abortado",name)
                pass
    else:
        items = soup.findAll("item")
        for item in items:
            try:
                videoTitle=item.title.string
                
            except:
                pass
            try:
                url=item.link.string
                
            except:
                pass
            try:
                thumbnail=item.thumbnail.string
                
            except:
                thumbnail=""
			
            listitem = xbmcgui.ListItem(videoTitle, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
            listitem.setInfo('video', {'videoTitle': videoTitle } )
            playList.add(url,listitem=listitem)
            addLink(videoTitle,url,thumbnail)

    #xbmc.executebuiltin("Container.SetViewMode(500)")
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
    
def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

def addDir(name,url,mode,iconimage,pasta=True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok

def get_url(std_url,file):
        url = std_url + "/ondemand/" + file
        paman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        paman.add_password(None, url, "xbmcuser", "user")
        authhandler = urllib2.HTTPBasicAuthHandler(paman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        response = urllib2.urlopen(url)
        link=response.read()
        response.close()
        return link

		

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]               
        return param
params=get_params()
url=None
name=None
mode=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

if mode==None or url==None or len(url)<1:
       
        main()
       
elif mode==2:
       
        lista(url)
        

xbmcplugin.endOfDirectory(int(sys.argv[1]))

