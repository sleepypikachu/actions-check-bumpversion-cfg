import pytest

import check_bumpversion_cfg as check


def test_parse_version():
    assert [1, 0, 0] == check.parse_version("1.0.0")


@pytest.mark.parametrize(
    "current, new",
    (
        ([1, 0, 0], [1, 0, 1]),
        ([1, 0, 0], [1, 1, 0]),
        ([1, 0, 0], [2, 0, 0]),
        ([1, 10, 0], [2, 0, 0]),
    ),
)
def test_new_greater_than_current_true(current, new):
    assert check.new_greater_than_current(current, new)


@pytest.mark.parametrize(
    "current, new",
    (
        ([2, 0, 0], [1, 100, 0]),
        ([2, 0, 1], [2, 0, 0]),
    ),
)
def test_new_greater_than_current_false(current, new):
    assert not check.new_greater_than_current(current, new)


def test_format_bumpversion_github_action_error():
    assert (
        check.format_bumpversion_github_action_error("foo")
        == "::error file=.bumpversion.cfg::foo"
    )
