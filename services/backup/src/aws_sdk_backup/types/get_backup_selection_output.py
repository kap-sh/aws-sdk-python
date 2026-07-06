"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupSelectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_selection
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class GetBackupSelectionOutput(TypedDict, closed=True):
    backup_selection: NotRequired[
        "aws_sdk_backup.types.backup_selection.BackupSelection"
    ]
    """<p>Specifies the body of a request to assign a set of resources to a backup plan.</p>"""
    selection_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Uniquely identifies the body of a request to assign a set of resources to a backup plan.</p>"""
    backup_plan_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Uniquely identifies a backup plan.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a backup selection is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    creator_request_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupSelectionOutput) -> dict:
    out: dict = {}
    if "backup_selection" in value:
        import aws_sdk_backup.types.backup_selection

        out["BackupSelection"] = aws_sdk_backup.types.backup_selection.serialize_json(
            value["backup_selection"]
        )
    if "selection_id" in value:
        out["SelectionId"] = value["selection_id"]
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    return out


def deserialize_json(data: dict) -> GetBackupSelectionOutput:
    out: GetBackupSelectionOutput = {}  # type: ignore[typeddict-item]
    if "BackupSelection" in data:
        import aws_sdk_backup.types.backup_selection

        out["backup_selection"] = (
            aws_sdk_backup.types.backup_selection.deserialize_json(
                data["BackupSelection"]
            )
        )
    if "SelectionId" in data:
        out["selection_id"] = data["SelectionId"]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    return out
