"""Generated from Smithy shape ``com.amazonaws.efs#UpdateFileSystemProtectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.replication_overwrite_protection


class UpdateFileSystemProtectionRequest(TypedDict):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system to update. </p>"""
    replication_overwrite_protection: NotRequired[
        "aws_sdk_efs.types.replication_overwrite_protection.ReplicationOverwriteProtection"
    ]
    """<p>The status of the file system's replication overwrite protection.</p> <ul> <li> <p> <code>ENABLED</code> – The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is <code>ENABLED</code> by default. </p> </li> <li> <p> <code>DISABLED</code> – The file system can be used as the destination file system in a replication configuration. The file system is read-only and can only be modified by EFS replication.</p> </li> <li> <p> <code>REPLICATING</code> – The file system is being used as the destination file system in a replication configuration. The file system is read-only and is only modified only by EFS replication.</p> </li> </ul> <p>If the replication configuration is deleted, the file system's replication overwrite protection is re-enabled and the file system becomes writeable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFileSystemProtectionRequest) -> dict:
    out: dict = {}
    if "replication_overwrite_protection" in value:
        import aws_sdk_efs.types.replication_overwrite_protection

        out["ReplicationOverwriteProtection"] = (
            aws_sdk_efs.types.replication_overwrite_protection.serialize_json(
                value["replication_overwrite_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFileSystemProtectionRequest:
    out: UpdateFileSystemProtectionRequest = {}  # type: ignore[typeddict-item]
    if "ReplicationOverwriteProtection" in data:
        import aws_sdk_efs.types.replication_overwrite_protection

        out["replication_overwrite_protection"] = (
            aws_sdk_efs.types.replication_overwrite_protection.deserialize_json(
                data["ReplicationOverwriteProtection"]
            )
        )
    return out
