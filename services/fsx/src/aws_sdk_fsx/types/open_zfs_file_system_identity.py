"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSFileSystemIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.open_zfs_file_system_user_type
    import aws_sdk_fsx.types.open_zfs_posix_file_system_user


class OpenZFSFileSystemIdentity(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_fsx.types.open_zfs_file_system_user_type.OpenZFSFileSystemUserType"
    ]
    """<p>Specifies the FSx for OpenZFS user identity type, accepts only <code>POSIX</code>.</p>"""
    posix_user: NotRequired[
        "aws_sdk_fsx.types.open_zfs_posix_file_system_user.OpenZFSPosixFileSystemUser"
    ]
    """<p>Specifies the UID and GIDs of the file system POSIX user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSFileSystemIdentity) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_fsx.types.open_zfs_file_system_user_type

        out["Type"] = (
            aws_sdk_fsx.types.open_zfs_file_system_user_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "posix_user" in value:
        import aws_sdk_fsx.types.open_zfs_posix_file_system_user

        out["PosixUser"] = (
            aws_sdk_fsx.types.open_zfs_posix_file_system_user.serialize_aws_json_1_1(
                value["posix_user"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSFileSystemIdentity:
    out: OpenZFSFileSystemIdentity = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_fsx.types.open_zfs_file_system_user_type

        out["type"] = (
            aws_sdk_fsx.types.open_zfs_file_system_user_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "PosixUser" in data:
        import aws_sdk_fsx.types.open_zfs_posix_file_system_user

        out["posix_user"] = (
            aws_sdk_fsx.types.open_zfs_posix_file_system_user.deserialize_aws_json_1_1(
                data["PosixUser"]
            )
        )
    return out
