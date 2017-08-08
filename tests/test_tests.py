# -*- coding: utf-8 -*-


def test_one(fixit):
    assert fixit


def test_addition():
    assert 1 + 1 == 2


def test_fail(fixit):
    assert not fixit
