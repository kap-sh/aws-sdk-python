"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreTestingPlansInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.list_restore_testing_plans_input_max_results_integer


class ListRestoreTestingPlansInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_backup.types.list_restore_testing_plans_input_max_results_integer.ListRestoreTestingPlansInputMaxResultsInteger"
    ]
    """<p>The maximum number of items to be returned.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the nexttoken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreTestingPlansInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRestoreTestingPlansInput:
    out: ListRestoreTestingPlansInput = {}  # type: ignore[typeddict-item]
    return out
