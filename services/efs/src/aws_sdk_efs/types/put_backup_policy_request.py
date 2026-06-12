"""Generated from Smithy shape ``com.amazonaws.efs#PutBackupPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.backup_policy
    import aws_sdk_efs.types.file_system_id


class PutBackupPolicyRequest(TypedDict):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>Specifies which EFS file system to update the backup policy for.</p>"""
    backup_policy: "aws_sdk_efs.types.backup_policy.BackupPolicy"
    """<p>The backup policy included in the <code>PutBackupPolicy</code> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutBackupPolicyRequest) -> dict:
    out: dict = {}
    import aws_sdk_efs.types.backup_policy

    out["BackupPolicy"] = aws_sdk_efs.types.backup_policy.serialize_json(
        value["backup_policy"]
    )
    return out


def deserialize_json(data: dict) -> PutBackupPolicyRequest:
    out: PutBackupPolicyRequest = {}  # type: ignore[typeddict-item]
    if "BackupPolicy" in data:
        import aws_sdk_efs.types.backup_policy

        out["backup_policy"] = aws_sdk_efs.types.backup_policy.deserialize_json(
            data["BackupPolicy"]
        )
    else:
        raise DeserializationError("PutBackupPolicyRequest.backup_policy required")
    return out
