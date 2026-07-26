"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupSelectionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_selections_list
    import capo_backup.types.string


class ListBackupSelectionsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    backup_selections_list: NotRequired[
        "capo_backup.types.backup_selections_list.BackupSelectionsList"
    ]
    """<p>An array of backup selection list items containing metadata about each resource in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupSelectionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "backup_selections_list" in value:
        import capo_backup.types.backup_selections_list

        out["BackupSelectionsList"] = (
            capo_backup.types.backup_selections_list.serialize_json(
                value["backup_selections_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBackupSelectionsOutput:
    out: ListBackupSelectionsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "BackupSelectionsList" in data:
        import capo_backup.types.backup_selections_list

        out["backup_selections_list"] = (
            capo_backup.types.backup_selections_list.deserialize_json(
                data["BackupSelectionsList"]
            )
        )
    return out
