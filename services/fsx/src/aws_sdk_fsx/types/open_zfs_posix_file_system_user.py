"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSPosixFileSystemUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_system_gid
    import aws_sdk_fsx.types.file_system_secondary_gi_ds
    import aws_sdk_fsx.types.file_system_uid


class OpenZFSPosixFileSystemUser(TypedDict, closed=True):
    uid: NotRequired["aws_sdk_fsx.types.file_system_uid.FileSystemUID"]
    """<p>The UID of the file system user.</p>"""
    gid: NotRequired["aws_sdk_fsx.types.file_system_gid.FileSystemGID"]
    """<p>The GID of the file system user.</p>"""
    secondary_gids: NotRequired[
        "aws_sdk_fsx.types.file_system_secondary_gi_ds.FileSystemSecondaryGIDs"
    ]
    """<p>The list of secondary GIDs for the file system user. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSPosixFileSystemUser) -> dict:
    out: dict = {}
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "gid" in value:
        out["Gid"] = value["gid"]
    if "secondary_gids" in value:
        import aws_sdk_fsx.types.file_system_secondary_gi_ds

        out["SecondaryGids"] = (
            aws_sdk_fsx.types.file_system_secondary_gi_ds.serialize_aws_json_1_1(
                value["secondary_gids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSPosixFileSystemUser:
    out: OpenZFSPosixFileSystemUser = {}  # type: ignore[typeddict-item]
    if "Uid" in data:
        out["uid"] = data["Uid"]
    if "Gid" in data:
        out["gid"] = data["Gid"]
    if "SecondaryGids" in data:
        import aws_sdk_fsx.types.file_system_secondary_gi_ds

        out["secondary_gids"] = (
            aws_sdk_fsx.types.file_system_secondary_gi_ds.deserialize_aws_json_1_1(
                data["SecondaryGids"]
            )
        )
    return out
