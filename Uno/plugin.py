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
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
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
    '''
        Add the help for '@plugin help Uno' here
        This should describe *how* to use this plugin.
    '''


    def start(self, irc):
        '''
            Starts a given game at the table in which the user has joined.
        '''
        pass
    start = wrap(start)

    def join(self, irc):
        '''
            Joins a table.
        '''
        pass
    join = wrap(join)

Class = Uno

class Game(object):
    '''
        Game object.

        Handles everything to do with the game.
        Deck, players, etc
    '''


    def __init__(self, table):
        self.__table = table
        self.__players = self.__table.players
        self.__deck = Deck()
        self.__reversed = false

    @property
    def reversed(self):
        '''
            Getter.
        '''
        return self.__reversed

    @reversed.setter
    def reversed(self, value):
        self.__reversed = value

class Table(object):

    def __init__(self):
        self._move = 0
        self._players = dict()
        self._info = {'creater': '',}

    @property
    def players(self):
        return self._players

    def add_user(self, player):
        '''
            Adds a new user to the table.
            @todo: Add support for checking if the user is on another table.
        '''
        if player.lower() not in self._players.keys():
            self._players[player.lower()] = Player(name, len(self._players))

    def next_move(self):
        pass


class Player(object):

    def __init__(self, name, id):
        self._name = name
        self._id = id
        self._hand = list()

    def play_card(self, name):
        pass

class Card(object):
    '''
        Base class for cards.
    '''
    pass

class Number_Card(Card):
    '''
        Number card.
    '''


    def __init__(self, number, colour):
        '''
            Constructor.
        '''
        self._number = number
        self._colour = colour

    @property
    def number(self):
        '''
            Getter
        '''
        return self._number

    @property
    def colour(self):
        '''
            Getter
        '''
        return self._colour

    def __str__(self):
        '''
            Returns a custom string representation of the object.
        '''
        return '{0}:{1}'.format(self._number, self._colour)

class Special_Card(Card):
    '''
        Special card object for cards such as skip, revers, draw two, wild
        and wild draw four.
    '''


    def __init__(self, special, colour):
        '''
            Constructor.
        '''
        self._special = special
        self._colour = colour
    
    @property
    def special(self):
        '''
            Getter.
        '''
        return self._special
    
    @property
    def colour(self):
        '''
            Getter.
        '''
        return self._colour
    
    def __str__(self):
        '''
            Returns a customs string representation of the object.
        '''
        return '{0}:{1}'.format(self._special, self._colour)

class Deck(object):
    '''
        Deck object.

        Handles all deck related opperations.
    '''


    def __init__(self):
        '''
            Constructor.
        '''
        self._list = list()
        self.init_list()
        self.shuffle()

    def init_list(self):
        '''
            Creates a new deck of cards, 108 in total.

            19 number cards of each colour - 0(x1) to 9(x2).
            8 draw two, reverse and skip cards.
            4 wild and wild draw four cards.
        '''
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


    def shuffle(self, count=1):
        '''
            Simply shuffles the deck.
            @todo: Possibly shuffle the deck multiple times.
        '''
        for i in range(count):
            random.shuffle(self._list, random.random)

class Error():
    '''
        Base class for all exceptions.
    '''
    pass

def enum(**enums):
    '''
        Creates and returns an enumerator.
    '''
    return type('Emum', (), enums)

# Simple enumerators...
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
