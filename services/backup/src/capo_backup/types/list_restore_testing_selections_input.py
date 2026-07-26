"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreTestingSelectionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.list_restore_testing_selections_input_max_results_integer


class ListRestoreTestingSelectionsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_backup.types.list_restore_testing_selections_input_max_results_integer.ListRestoreTestingSelectionsInputMaxResultsInteger"
    ]
    """<p>The maximum number of items to be returned.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the nexttoken.</p>"""
    restore_testing_plan_name: "str"
    """<p>Returns restore testing selections by the specified restore testing plan name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreTestingSelectionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRestoreTestingSelectionsInput:
    out: ListRestoreTestingSelectionsInput = {}  # type: ignore[typeddict-item]
    return out
