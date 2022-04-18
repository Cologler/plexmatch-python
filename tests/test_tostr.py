# -*- coding: utf-8 -*-
#
# Copyright (c) 2022~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os

from plexmatch import tostr, PlexMatch

def test_tostr_empty():
    plex_match = PlexMatch()
    assert tostr(plex_match) == ''

def test_tostr_show():
    plex_match = PlexMatch()
    plex_match.show = ''
    assert tostr(plex_match) == 'show: '

    plex_match = PlexMatch()
    plex_match.show = 'fasgd'
    assert tostr(plex_match) == 'show: fasgd'

def test_tostr_season():
    plex_match = PlexMatch()
    plex_match.season = 0
    assert tostr(plex_match) == 'season: 0'

    plex_match = PlexMatch()
    plex_match.season = 1
    assert tostr(plex_match) == 'season: 1'

def _create_plex_match_with_episodes():
    plex_match = PlexMatch()
    plex_match.add_episode('hg53hjf', 1, 1)
    plex_match.add_episode('grehger', 2, 1)
    plex_match.add_episode('htrnfge', 3, 1)
    return plex_match

def test_tostr_episodes():
    plex_match = _create_plex_match_with_episodes()
    plex_match.add_episode('morecallnth', 2, 3, 4, 5)
    assert tostr(plex_match) == os.linesep.join([
        'episode: S01E01: hg53hjf',
        'episode: S01E02: grehger',
        'episode: S01E03: htrnfge',
        'episode: S03E02-S05E04: morecallnth'
    ])

def test_tostr_episodes_with_season():
    plex_match = _create_plex_match_with_episodes()
    plex_match.season = 1
    assert tostr(plex_match) == os.linesep.join([
        'season: 1',
        'episode: E01: hg53hjf',
        'episode: E02: grehger',
        'episode: E03: htrnfge',
    ])

def test_tostr_episodes_with_unmatch_season():
    plex_match = _create_plex_match_with_episodes()
    plex_match.season = 2
    assert tostr(plex_match) == os.linesep.join([
        'season: 2',
        'episode: S01E01: hg53hjf',
        'episode: S01E02: grehger',
        'episode: S01E03: htrnfge',
    ])

def test_tostr_mulit_season_episodes_with_season():
    plex_match = _create_plex_match_with_episodes()
    plex_match.season = 2
    plex_match.add_episode('month', 2, 3)
    plex_match.add_episode('tonight', 1, 3)
    plex_match.add_episode('position', 3, 3)
    plex_match.add_episode('flow', 3, 2)
    plex_match.add_episode('sleep', 2, 2)
    plex_match.add_episode('terrible', 1, 2)
    assert tostr(plex_match) == os.linesep.join([
        'season: 2',
        'episode: S01E01: hg53hjf',
        'episode: S01E02: grehger',
        'episode: S01E03: htrnfge',
        'episode: S03E02: month',
        'episode: S03E01: tonight',
        'episode: S03E03: position',
        'episode: S02E03: flow',
        'episode: S02E02: sleep',
        'episode: S02E01: terrible',
    ])

def test_tostr_episodes_with_sort():
    plex_match = _create_plex_match_with_episodes()
    plex_match.add_episode('month', 2, 3)
    plex_match.add_episode('tonight', 1, 3)
    plex_match.add_episode('position', 3, 3)
    plex_match.add_episode('flow', 3, 2)
    plex_match.add_episode('sleep', 2, 2)
    plex_match.add_episode('terrible', 1, 2)
    assert tostr(plex_match, sort_episodes=True) == os.linesep.join([
        'episode: S01E01: hg53hjf',
        'episode: S01E02: grehger',
        'episode: S01E03: htrnfge',
        'episode: S02E01: terrible',
        'episode: S02E02: sleep',
        'episode: S02E03: flow',
        'episode: S03E01: tonight',
        'episode: S03E02: month',
        'episode: S03E03: position',
    ])

def test_tostr_imdb_id():
    plex_match = PlexMatch()
    plex_match.imdbid = 'tt0123456'
    assert tostr(plex_match) == 'imdbid: tt0123456'

def test_tostr_tvdb_id():
    plex_match = PlexMatch()
    plex_match.tvdbid = '0123456'
    assert tostr(plex_match) == 'tvdbid: 0123456'

def test_tostr_tmdb_id():
    plex_match = PlexMatch()
    plex_match.tmdbid = '0123456'
    assert tostr(plex_match) == 'tmdbid: 0123456'

def test_tostr_year():
    plex_match = PlexMatch()
    plex_match.year = 2020
    assert tostr(plex_match) == 'year: 2020'

def test_tostr_guid():
    plex_match = PlexMatch()
    plex_match.guid = 'plex://show/grerehrtjyrtjktyk51435561435'
    assert tostr(plex_match) == 'guid: plex://show/grerehrtjyrtjktyk51435561435'
