"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteBackupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.backup_id
    import capo_fsx.types.backup_lifecycle


class DeleteBackupResponse(TypedDict, closed=True):
    backup_id: NotRequired["capo_fsx.types.backup_id.BackupId"]
    """<p>The ID of the backup that was deleted.</p>"""
    lifecycle: NotRequired["capo_fsx.types.backup_lifecycle.BackupLifecycle"]
    """<p>The lifecycle status of the backup. If the <code>DeleteBackup</code> operation is successful, the status is <code>DELETED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBackupResponse) -> dict:
    out: dict = {}
    if "backup_id" in value:
        out["BackupId"] = value["backup_id"]
    if "lifecycle" in value:
        import capo_fsx.types.backup_lifecycle

        out["Lifecycle"] = capo_fsx.types.backup_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBackupResponse:
    out: DeleteBackupResponse = {}  # type: ignore[typeddict-item]
    if "BackupId" in data:
        out["backup_id"] = data["BackupId"]
    if "Lifecycle" in data:
        import capo_fsx.types.backup_lifecycle

        out["lifecycle"] = capo_fsx.types.backup_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    return out
