#!/bin/python
import xbmcplugin,xbmcgui,xbmc,xbmcaddon,webbrowser,os,sys

addon = xbmcaddon.Addon('plugin.video.live.streamspro')
pfad = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
icon = xbmc.translatePath(pfad + "/resources/lib/reg.png")

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
    webbrowser.open_new('http://forum.freetvbrasil.com')
elif os == 'linux':
    webbrowser.open_new('http://forum.freetvbrasil.com')
elif os == 'android':
    xbmc.executebuiltin('XBMC.Notification(Registrar:, forum http://forum.freetvbrasil.com ,30000,'+icon+')')
elif os == 'darwin' or os == 'ios' or os == 'atv2':
    webbrowser.open_new('http://forum.freetvbrasil.com')
else:
    xbmc.executebuiltin('XBMC.Notification(Registrar:, forum http://forum.freetvbrasil.com ,30000,'+icon+')')