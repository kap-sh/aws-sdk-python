"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemProtectionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.replication_overwrite_protection


class FileSystemProtectionDescription(TypedDict, closed=True):
    replication_overwrite_protection: NotRequired[
        "capo_efs.types.replication_overwrite_protection.ReplicationOverwriteProtection"
    ]
    """<p>The status of the file system's replication overwrite protection.</p> <ul> <li> <p> <code>ENABLED</code> – The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is <code>ENABLED</code> by default. </p> </li> <li> <p> <code>DISABLED</code> – The file system can be used as the destination file system in a replication configuration. The file system is read-only and can only be modified by EFS replication.</p> </li> <li> <p> <code>REPLICATING</code> – The file system is being used as the destination file system in a replication configuration. The file system is read-only and is modified only by EFS replication.</p> </li> </ul> <p>If the replication configuration is deleted, the file system's replication overwrite protection is re-enabled, the file system becomes writeable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemProtectionDescription) -> dict:
    out: dict = {}
    if "replication_overwrite_protection" in value:
        import capo_efs.types.replication_overwrite_protection

        out["ReplicationOverwriteProtection"] = (
            capo_efs.types.replication_overwrite_protection.serialize_json(
                value["replication_overwrite_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> FileSystemProtectionDescription:
    out: FileSystemProtectionDescription = {}  # type: ignore[typeddict-item]
    if "ReplicationOverwriteProtection" in data:
        import capo_efs.types.replication_overwrite_protection

        out["replication_overwrite_protection"] = (
            capo_efs.types.replication_overwrite_protection.deserialize_json(
                data["ReplicationOverwriteProtection"]
            )
        )
    return out
