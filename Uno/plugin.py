###
# Copyright (c) 2013, ki113d
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring

import random

_ = PluginInternationalization('Uno')


@internationalizeDocstring
class Uno(callbacks.Plugin):
    """Add the help for "@plugin help Uno" here
    This should describe *how* to use this plugin."""
    pass

    def start(self, irc):
        
        pass
    start = wrap(start)


Class = Uno

class Game(object):
    pass

class Table(object):

    def __init__(self):
        self._move = 0
        self._players = dict()
        self._info = {'creater', '';}

    @property
    def players(self):
        return self._players

    def add_user(self, player):
        if player.lower() not in self._players.keys():
            self._players[player.lower()] = Player(name, len(self._players))

    def next_move(self):
        if len(self._players) < 2:


class Player(object):

    def __init__(self, name, id):
        self._name = name
        self._id = id

class Card(object):
    """
        Base class for cards.
    """
    pass

class Number_Card(Card):
    def __init__(self, number, colour):
        self._number = number
        self._colour = colour

    @property
    def number(self):
        return self._number

    @property
    def colour(self):
        return self._colour

    def __str__(self):
        return '{0}:{1}'.format(self._number, self._colour)

class Special_Card(Card):
    def __init__(self, special, colour):
        self._special = special
        self._colour = colour
    
    @property
    def special(self):
        return self._special
    
    @property
    def colour(self):
        return self._colour
    
    def __str__(self):
        return '{0}:{1}'.format(self._special, self._colour)

class Deck(object):

    def __init__(self):
        self._list = list()

    def init_list(self):
        # Set up deck with coloured cards.
        for colour in (Colours.BLUE, Colours.GREEN, Colours.RED, Colours.YELLOW):
            for number in xrange(10):
                self._list.exted(Number_Card(number, colour)
                if number >  0:
                    self._list.extend(Number_Card(number, colour)
            for special in (Specials.DRAW_TWO, Specials.REVERSE, Specials.SKIP):
                for number in xrange(2):
                    self._list.extend(Special_Card(special, colour))
        # And finally wild cards.
        for special in (Specials.WILD, Special.WILD_DRAW_FOUR):
            for x in xrange(4):
                self._list.extend(Special_Card(special, Colours.NONE)


    def shuffle(self):
        random.shuffle(self._list, random.random)

class Error():
    '''
        Base class for all exceptions.
    '''
    pass

def enum(**enums):
    return type('Emum', (), enums)

Colours = enum(BLUE='Blue',
               GREEN='Green',
               RED='Red',
               YELLOW='Yellow',
               NONE='None')

Specials = enum(DRAW_TWO='Draw Two',
                REVERSE='Reverse',
                SKIP='Skip',
                WILD='Wild',
                WILD_DRAW_FOUR= 'Wild Draw Four')

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
