MODULES = ['main', 'backend']

DEPS =  [
    (['any'],
     [
        ('plugin', 'services'),
        ('app', 'dnsmasq', 'dnsmasq')
     ])
]
NAME = 'Dnsmasq'
PLATFORMS = ['any']
DESCRIPTION = 'dnsmasq configuration'
VERSION = '1'
GENERATION = 1
AUTHOR = 'Ajenti team'
HOMEPAGE = 'http://ajenti.org'
