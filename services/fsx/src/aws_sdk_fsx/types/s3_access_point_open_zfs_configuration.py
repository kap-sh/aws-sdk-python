"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointOpenZFSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.open_zfs_file_system_identity
    import aws_sdk_fsx.types.volume_id


class S3AccessPointOpenZFSConfiguration(TypedDict, closed=True):
    volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the FSx for OpenZFS volume that the S3 access point is attached to.</p>"""
    file_system_identity: NotRequired[
        "aws_sdk_fsx.types.open_zfs_file_system_identity.OpenZFSFileSystemIdentity"
    ]
    """<p>The file system identity used to authorize file access requests made using the S3 access point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointOpenZFSConfiguration) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "file_system_identity" in value:
        import aws_sdk_fsx.types.open_zfs_file_system_identity

        out["FileSystemIdentity"] = (
            aws_sdk_fsx.types.open_zfs_file_system_identity.serialize_aws_json_1_1(
                value["file_system_identity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3AccessPointOpenZFSConfiguration:
    out: S3AccessPointOpenZFSConfiguration = {}  # type: ignore[typeddict-item]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "FileSystemIdentity" in data:
        import aws_sdk_fsx.types.open_zfs_file_system_identity

        out["file_system_identity"] = (
            aws_sdk_fsx.types.open_zfs_file_system_identity.deserialize_aws_json_1_1(
                data["FileSystemIdentity"]
            )
        )
    return out
