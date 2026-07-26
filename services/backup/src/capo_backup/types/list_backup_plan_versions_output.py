"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupPlanVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_plan_versions_list
    import capo_backup.types.string


class ListBackupPlanVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    backup_plan_versions_list: NotRequired[
        "capo_backup.types.backup_plan_versions_list.BackupPlanVersionsList"
    ]
    """<p>An array of version list items containing metadata about your backup plans.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupPlanVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "backup_plan_versions_list" in value:
        import capo_backup.types.backup_plan_versions_list

        out["BackupPlanVersionsList"] = (
            capo_backup.types.backup_plan_versions_list.serialize_json(
                value["backup_plan_versions_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBackupPlanVersionsOutput:
    out: ListBackupPlanVersionsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "BackupPlanVersionsList" in data:
        import capo_backup.types.backup_plan_versions_list

        out["backup_plan_versions_list"] = (
            capo_backup.types.backup_plan_versions_list.deserialize_json(
                data["BackupPlanVersionsList"]
            )
        )
    return out
