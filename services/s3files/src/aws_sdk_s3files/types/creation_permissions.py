"""Generated from Smithy shape ``com.amazonaws.s3files#CreationPermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.owner_gid
    import aws_sdk_s3files.types.owner_uid
    import aws_sdk_s3files.types.permissions


class CreationPermissions(TypedDict, closed=True):
    owner_uid: "aws_sdk_s3files.types.owner_uid.OwnerUid"
    """<p>The POSIX user ID to assign to newly created directories.</p>"""
    owner_gid: "aws_sdk_s3files.types.owner_gid.OwnerGid"
    """<p>The POSIX group ID to assign to newly created directories.</p>"""
    permissions: "aws_sdk_s3files.types.permissions.Permissions"
    """<p>The octal permissions to assign to newly created directories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreationPermissions) -> dict:
    out: dict = {}
    out["ownerUid"] = value["owner_uid"]
    out["ownerGid"] = value["owner_gid"]
    out["permissions"] = value["permissions"]
    return out


def deserialize_json(data: dict) -> CreationPermissions:
    out: CreationPermissions = {}  # type: ignore[typeddict-item]
    if "ownerUid" in data:
        out["owner_uid"] = data["ownerUid"]
    else:
        raise DeserializationError("CreationPermissions.owner_uid required")
    if "ownerGid" in data:
        out["owner_gid"] = data["ownerGid"]
    else:
        raise DeserializationError("CreationPermissions.owner_gid required")
    if "permissions" in data:
        out["permissions"] = data["permissions"]
    else:
        raise DeserializationError("CreationPermissions.permissions required")
    return out
