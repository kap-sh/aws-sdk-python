"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupSelectionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.max_results
    import capo_backup.types.string


class ListBackupSelectionsInput(TypedDict, closed=True):
    backup_plan_id: "capo_backup.types.string.string"
    """<p>Uniquely identifies a backup plan.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupSelectionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBackupSelectionsInput:
    out: ListBackupSelectionsInput = {}  # type: ignore[typeddict-item]
    return out
