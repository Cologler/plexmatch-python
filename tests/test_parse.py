# -*- coding: utf-8 -*-
#
# Copyright (c) 2022~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from plexmatch import parse, PlexMatch

def test_parse_empty():
    assert parse('') == PlexMatch()

def test_parse_show():
    assert parse('show: fasgd') == PlexMatch(show='fasgd')

def test_parse_year():
    assert parse('year: 2020') == PlexMatch(year=2020)

def test_parse_season():
    assert parse('season: 1') == PlexMatch(season=1)

def test_parse_episode():
    plex_match = PlexMatch()
    plex_match.add_episode('bsfgsfg', 1, 1)
    plex_match.add_episode('hg53hjf', 2, 3)
    plex_match.add_episode('fdj655i', 4, 5)
    assert parse('''
        episode: S01E01: bsfgsfg
        episode: S03E02: hg53hjf
        episode: S05E04: fdj655i
    ''') == plex_match
