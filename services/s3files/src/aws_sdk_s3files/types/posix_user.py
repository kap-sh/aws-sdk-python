"""Generated from Smithy shape ``com.amazonaws.s3files#PosixUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.gid
    import aws_sdk_s3files.types.secondary_gids
    import aws_sdk_s3files.types.uid


class PosixUser(TypedDict, closed=True):
    uid: "aws_sdk_s3files.types.uid.Uid"
    """<p>The POSIX user ID.</p>"""
    gid: "aws_sdk_s3files.types.gid.Gid"
    """<p>The POSIX group ID.</p>"""
    secondary_gids: NotRequired["aws_sdk_s3files.types.secondary_gids.SecondaryGids"]
    """<p>An array of secondary POSIX group IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PosixUser) -> dict:
    out: dict = {}
    out["uid"] = value["uid"]
    out["gid"] = value["gid"]
    if "secondary_gids" in value:
        import aws_sdk_s3files.types.secondary_gids

        out["secondaryGids"] = aws_sdk_s3files.types.secondary_gids.serialize_json(
            value["secondary_gids"]
        )
    return out


def deserialize_json(data: dict) -> PosixUser:
    out: PosixUser = {}  # type: ignore[typeddict-item]
    if "uid" in data:
        out["uid"] = data["uid"]
    else:
        raise DeserializationError("PosixUser.uid required")
    if "gid" in data:
        out["gid"] = data["gid"]
    else:
        raise DeserializationError("PosixUser.gid required")
    if "secondaryGids" in data:
        import aws_sdk_s3files.types.secondary_gids

        out["secondary_gids"] = aws_sdk_s3files.types.secondary_gids.deserialize_json(
            data["secondaryGids"]
        )
    return out
