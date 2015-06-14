#!/bin/python
import xbmcplugin,xbmcgui,xbmc,xbmcaddon,webbrowser,os,sys

addon = xbmcaddon.Addon('plugin.video.live.streamspro')
pfad = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
icon = xbmc.translatePath(pfad + "/resources/lib/pp.png")

if xbmc.getCondVisibility("system.platform.android"):
    os = "android"
elif xbmc.getCondVisibility("system.platform.linux"):
    os = "linux"
elif xbmc.getCondVisibility("system.platform.xbox"):
    os = "xbox"
elif xbmc.getCondVisibility("system.platform.windows"):
    os = "windows"
elif xbmc.getCondVisibility("system.platform.osx"):
    os = "darwin"
elif xbmc.getCondVisibility("system.platform.ios"):
    os = "ios"
elif xbmc.getCondVisibility("system.platform.atv2"):
    os = "atv2"


if os == 'windows':
    webbrowser.open_new('http://facebook.com/groups/tv.online.xbmc.brasil')
elif os == 'linux':
    webbrowser.open_new('http://facebook.com/groups/tv.online.xbmc.brasil')
elif os == 'android':
    xbmc.executebuiltin('XBMC.Notification(grupo:, facebook http://facebook.com/groups/tv.online.xbmc.brasil ,20000,'+icon+')')
elif os == 'darwin' or os == 'ios' or os == 'atv2':
    webbrowser.open_new('http://facebook.com/groups/tv.online.xbmc.brasil')
else:
    xbmc.executebuiltin('XBMC.Notification(grupo:, facebook http://facebook.com/groups/tv.online.xbmc.brasil ,20000,'+icon+')')