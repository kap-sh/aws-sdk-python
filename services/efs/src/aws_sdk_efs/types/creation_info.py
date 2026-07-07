"""Generated from Smithy shape ``com.amazonaws.efs#CreationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.owner_gid
    import aws_sdk_efs.types.owner_uid
    import aws_sdk_efs.types.permissions


class CreationInfo(TypedDict, closed=True):
    owner_uid: "aws_sdk_efs.types.owner_uid.OwnerUid"
    """<p>Specifies the POSIX user ID to apply to the <code>RootDirectory</code>. Accepts values from 0 to 2^32 (4294967295).</p>"""
    owner_gid: "aws_sdk_efs.types.owner_gid.OwnerGid"
    """<p>Specifies the POSIX group ID to apply to the <code>RootDirectory</code>. Accepts values from 0 to 2^32 (4294967295).</p>"""
    permissions: "aws_sdk_efs.types.permissions.Permissions"
    """<p>Specifies the POSIX permissions to apply to the <code>RootDirectory</code>, in the format of an octal number representing the file's mode bits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreationInfo) -> dict:
    out: dict = {}
    out["OwnerUid"] = value["owner_uid"]
    out["OwnerGid"] = value["owner_gid"]
    out["Permissions"] = value["permissions"]
    return out


def deserialize_json(data: dict) -> CreationInfo:
    out: CreationInfo = {}  # type: ignore[typeddict-item]
    if "OwnerUid" in data:
        out["owner_uid"] = data["OwnerUid"]
    else:
        raise DeserializationError("CreationInfo.owner_uid required")
    if "OwnerGid" in data:
        out["owner_gid"] = data["OwnerGid"]
    else:
        raise DeserializationError("CreationInfo.owner_gid required")
    if "Permissions" in data:
        out["permissions"] = data["Permissions"]
    else:
        raise DeserializationError("CreationInfo.permissions required")
    return out
