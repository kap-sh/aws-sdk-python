"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupPlanTemplatesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.max_results
    import aws_sdk_backup.types.string


class ListBackupPlanTemplatesInput(TypedDict):
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["aws_sdk_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupPlanTemplatesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBackupPlanTemplatesInput:
    out: ListBackupPlanTemplatesInput = {}  # type: ignore[typeddict-item]
    return out
