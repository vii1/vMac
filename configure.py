targets = {
    # ( description, cpu_family, target_family )
    'carb': ( "MacOS Carbon lib for OS 9 and OS X", 'ppc', 'carb' ),
    'cygw': ( "Cygwin/X", 'x86', 'cygw' ),
    'db64': ( "Dragonfly BSD for x64", 'x64', 'dbsd' ),
    'dbsd': ( "Dragonfly BSD for x86", 'x86', 'dbsd' ),
    'fb64': ( "FreeBSD for x64", 'x64', 'fbsd' ),
    'fbpc': ( "FreeBSD for PowerPC", 'ppc', 'fbsd' ),
    'fbsd': ( "FreeBSD for x86", 'x86', 'fbsd' ),
    'imch': ( "MacOS X Intel", 'x86', 'mach' ),
    'irix': ( "Silicon Graphics's IRIX on MIPS", 'mip', 'irix' ),
    'larm': ( "X11 for linux on arm (debian armel)", 'arm', 'linx' ),
    'lppc': ( "X11 for linux on PowerPC", 'ppc', 'linx' ),
    'lspr': ( "X11 for linux on SPARC", 'spr', 'linx' ),
    'lx64': ( "X11 for linux on x64", 'x64', 'linx' ),
    'lx86': ( "X11 for linux on x86", 'x86', 'linx' ),
    'm68k': ( "MacOS 68K", '68k', 'cmac' ),
    'mach': ( "MacOS X Macho", 'ppc', 'mach' ),
    'mc64': ( "MacOS X for x64", 'x64', 'mach' ),
    'mfpu': ( "MacOS 68K with FPU", '68k', 'cmac' ),
    'mi11': ( "X11 for MacOS X Intel", 'x86', 'mx11' ),
    'minx': ( "Minix on x86", 'x86', 'minx' ),
    'mppc': ( "MacOS OS 9 for PowerPC", 'ppc', 'cmac' ),
    'mx11': ( "X11 for MacOS X PowerPC", 'ppc', 'mx11' ),
    'mx64': ( "X11 for MacOS X x64", 'x64', 'mx64' ),
    'nb64': ( "NetBSD for x64", 'x64', 'nbsd' ),
    'nbsd': ( "NetBSD for x86", 'x86', 'nbsd' ),
    'ndsa': ( "Nintendo DS on ARM ", 'arm', 'lnds' ),
    'ob64': ( "OpenBSD for x64", 'x64', 'obsd' ),
    'obsd': ( "OpenBSD for x86", 'x86', 'obsd' ),
    'oi64': ( "OpenIndiana for x64", 'x64', 'oind' ),
    'oind': ( "OpenIndiana for x86", 'x86', 'oind' ),
    'sl86': ( "Solaris Intel", 'x86', 'slrs' ),
    'slrs': ( "Solaris SPARC", 'spr', 'slrs' ),
    'wc86': ( "Windows CE (emulator) on x86", 'x86', 'wnce' ),
    'wcar': ( "Windows CE on ARM", 'arm', 'wnce' ),
    'wx64': ( "Windows on x64", 'x64', 'mswn' ),
    'wx86': ( "Windows", 'x86', 'mswn' ),
    'xgen': ( "Generic X11", 'gen', 'xgen' ),
}

cpu_families = {
    '68k': "Motorola 680x0",
    'ppc': "PowerPC",
    'x86': "Intel 80x86",
    'spr': "SPARC",
    'arm': "ARM",
    'x64': "x86-64 (aka AMD64, Intel 64)",
    'mip': "MIPS",
    'gen': "Generic (don't know)",
}

target_families = {
    # ( description, default_ide )
    'carb': ( "MacOS Carbon lib for OS 9 and OS X", 'mpw' ),
    'cmac': ( "Classic Mac", 'mpw' ),
    'cygw': ( "Cygwin/X", 'cyg' ),
    'dbsd': ( "Dragonfly BSD", 'bgc' ),
    'fbsd': ( "FreeBSD", 'bgc' ),
    'irix': ( "Silicon Graphics's IRIX", 'bgc' ),
    'linx': ( "Linux", 'bgc' ),
    'lnds': ( "libnds for Nintendo DS", 'dkp' ),
    'mach': ( "OS X Macho", 'xcd' ),
    'minx': ( "Minix", 'bgc' ),
    'mswn': ( "Microsoft Windows", 'msv' ),
    'mx11': ( "X11 for MacOS X", 'xcd' ),
    'nbsd': ( "NetBSD", 'bgc' ),
    'obsd': ( "OpenBSD", 'bgc' ),
    'oind': ( "OpenIndiana", 'bgc' ),
    'slrs': ( "Solaris", 'bgc' ),
    'wnce': ( "Windows CE", 'msv' ),
    'xgen': ( "Generic X11", 'ccc' ),
}

ides = {
    # ( description, default_version )
    'mpw': ( "Macintosh Programmers Workshop", 1 ),
    'mw8': ( "Metrowerks CodeWarrior", 1 ),
    'bgc': ( "Gnu tools", 1 ),
    'snc': ( "Sun tools", 1 ),
    'msv': ( "Microsoft Visual C++", 8000 ),
    'lcc': ( "lcc-win32 - Jacob Navia", 1 ),
    'dvc': ( "Bloodshed Dev-C++", 1 ),
    'xcd': ( "Apple XCode", 2410 ),
    'dmc': ( "Digital Mars Compiler", 1 ),
    'plc': ( "Pelles C Compiler", 1 ),
    'mgw': ( "MinGW", 1 ),
    'cyg': ( "Cygwin", 1 ),
    'dkp': ( "devkitpro", 1 ),
    'ccc': ( "Generic command line c compiler", 1 ),
    'mvc': ( "Mini vMac C (a specific version of gcc)", 1 ),
}

api_families = {
    'mac',
    'osx',
    'win',
    'xwn',
    'nds',
    'gtk',
    'sdl',
    'sd2',
    'cco',
}

def get_default_api_family( target_family, cpu_family ):
    return {
        'cmac': 'mac',
        'mach': 'cco' if cpu_family=='x64' else 'osx',
        'carb': 'cco' if cpu_family=='x64' else 'osx',
        'mswn': 'win',
        'wnce': 'win',
        'linx': 'xwn',
        'slrs': 'xwn',
        'fbsd': 'xwn',
        'obsd': 'xwn',
        'nbsd': 'xwn',
        'dbsd': 'xwn',
        'oind': 'xwn',
        'minx': 'xwn',
        'irix': 'xwn',
        'mx11': 'xwn',
        'cygw': 'xwn',
        'xgen': 'xwn',
        'lnds': 'nds',
    }.get(target_family)

debug_levels = {
    'off',
    'test',
    'on'
}

languages = {
    'eng',
    'fre',
    'ita',
    'ger',
    'dut',
    'spa',
    'pol',
    'ptb',
}

def get_lproj_name(language):
    return {
        'eng': 'English',
        'fre': 'French',
        'ita': 'Italian',
        'ger': 'German',
        'dut': 'Dutch',
        'spa': 'Spanish',
        'pol': 'pl',
        'ptb': 'pt_BR',
    }.get(language)

eols = { 'mac', 'win', 'unx' }
