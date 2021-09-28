import pytest

@pytest.mark.xfail(condition=False, reason=None)
def test_succeed():
    assert False


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False