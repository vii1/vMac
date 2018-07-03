/*
	Configuration options used by platform specific code.

	This file is automatically generated by the build system,
	which tries to know what options are valid in what
	combinations. Avoid changing this file manually unless
	you know what you're doing.
*/

#define _CRT_SECURE_NO_DEPRECATE 1

/* ignore warning generated by system includes */
#pragma warning(push)
#pragma warning(disable : 4201 4115 4214)

#include <windows.h>
#include <time.h>
#include <shlobj.h>
#include <tchar.h>

/* restore warnings */
#pragma warning(pop)


#define RomFileName "vMac.ROM"
#define EnableDragDrop 1
#define EnableAltKeysMode 0
#define SwapCommandControl 0
#define VarFullScreen 1
#define WantInitFullScreen 0
#define MayFullScreen 1
#define MayNotFullScreen 1
#define WantInitMagnify 0
#define EnableMagnify 1
#define MyWindowScale 2
#define WantInitRunInBackground 0
#define WantInitNotAutoSlow 0
#define WantInitSpeedValue 3
#define NeedRequestInsertDisk 1
#define NeedDoMoreCommandsMsg 1
#define NeedDoAboutMsg 1
#define UseControlKeys 1
#define UseActvCode 0
#define EnableDemoMsg 0

/* version and other info to display to user */

#define NeedIntlChars 1
#define ItnlKyBdFix 1
#define kStrAppName "Mini vMac"
#define kAppVariationStr "minivmac-3.5.8-wx64"
#define kStrCopyrightYear "2017"
#define kMaintainerName "unknown"
#define kStrHomePage "http://www.gryphel.com/c/minivmac/"
