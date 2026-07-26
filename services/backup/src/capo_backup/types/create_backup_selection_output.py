"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupSelectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string
    import capo_backup.types.timestamp


class CreateBackupSelectionOutput(TypedDict, closed=True):
    selection_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies the body of a request to assign a set of resources to a backup plan.</p>"""
    backup_plan_id: NotRequired["capo_backup.types.string.string"]
    """<p>The ID of the backup plan.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a backup selection is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupSelectionOutput) -> dict:
    out: dict = {}
    if "selection_id" in value:
        out["SelectionId"] = value["selection_id"]
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> CreateBackupSelectionOutput:
    out: CreateBackupSelectionOutput = {}  # type: ignore[typeddict-item]
    if "SelectionId" in data:
        out["selection_id"] = data["SelectionId"]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "CreationDate" in data:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    return out
