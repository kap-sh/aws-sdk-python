"""Generated from Smithy shape ``com.amazonaws.fsx#CreateAndAttachS3AccessPointOpenZFSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.open_zfs_file_system_identity
    import capo_fsx.types.volume_id


class CreateAndAttachS3AccessPointOpenZFSConfiguration(TypedDict, closed=True):
    volume_id: NotRequired["capo_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the FSx for OpenZFS volume to which you want the S3 access point attached.</p>"""
    file_system_identity: NotRequired[
        "capo_fsx.types.open_zfs_file_system_identity.OpenZFSFileSystemIdentity"
    ]
    """<p>Specifies the file system user identity to use for authorizing file read and write requests that are made using this S3 access point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateAndAttachS3AccessPointOpenZFSConfiguration,
) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "file_system_identity" in value:
        import capo_fsx.types.open_zfs_file_system_identity

        out["FileSystemIdentity"] = (
            capo_fsx.types.open_zfs_file_system_identity.serialize_aws_json_1_1(
                value["file_system_identity"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateAndAttachS3AccessPointOpenZFSConfiguration:
    out: CreateAndAttachS3AccessPointOpenZFSConfiguration = {}  # type: ignore[typeddict-item]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "FileSystemIdentity" in data:
        import capo_fsx.types.open_zfs_file_system_identity

        out["file_system_identity"] = (
            capo_fsx.types.open_zfs_file_system_identity.deserialize_aws_json_1_1(
                data["FileSystemIdentity"]
            )
        )
    return out
