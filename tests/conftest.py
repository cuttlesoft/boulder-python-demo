# -*- coding: utf-8 -*-

import pytest


@pytest.fixture()
def fixit():
    fixture_var = True
    return fixture_var
