"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupPlansOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_plans_list
    import capo_backup.types.string


class ListBackupPlansOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    backup_plans_list: NotRequired[
        "capo_backup.types.backup_plans_list.BackupPlansList"
    ]
    """<p>Information about the backup plans.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupPlansOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "backup_plans_list" in value:
        import capo_backup.types.backup_plans_list

        out["BackupPlansList"] = capo_backup.types.backup_plans_list.serialize_json(
            value["backup_plans_list"]
        )
    return out


def deserialize_json(data: dict) -> ListBackupPlansOutput:
    out: ListBackupPlansOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "BackupPlansList" in data:
        import capo_backup.types.backup_plans_list

        out["backup_plans_list"] = capo_backup.types.backup_plans_list.deserialize_json(
            data["BackupPlansList"]
        )
    return out
