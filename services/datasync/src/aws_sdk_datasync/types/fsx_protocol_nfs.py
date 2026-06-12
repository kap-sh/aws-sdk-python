"""Generated from Smithy shape ``com.amazonaws.datasync#FsxProtocolNfs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.nfs_mount_options


class FsxProtocolNfs(TypedDict):
    mount_options: NotRequired[
        "aws_sdk_datasync.types.nfs_mount_options.NfsMountOptions"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FsxProtocolNfs) -> dict:
    out: dict = {}
    if "mount_options" in value:
        import aws_sdk_datasync.types.nfs_mount_options

        out["MountOptions"] = (
            aws_sdk_datasync.types.nfs_mount_options.serialize_aws_json_1_1(
                value["mount_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FsxProtocolNfs:
    out: FsxProtocolNfs = {}  # type: ignore[typeddict-item]
    if "MountOptions" in data:
        import aws_sdk_datasync.types.nfs_mount_options

        out["mount_options"] = (
            aws_sdk_datasync.types.nfs_mount_options.deserialize_aws_json_1_1(
                data["MountOptions"]
            )
        )
    return out
