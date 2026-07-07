"""Generated from Smithy shape ``com.amazonaws.transfer#PosixProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.posix_id
    import aws_sdk_transfer.types.secondary_gids


class PosixProfile(TypedDict, closed=True):
    uid: "aws_sdk_transfer.types.posix_id.PosixId"
    """<p>The POSIX user ID used for all EFS operations by this user.</p>"""
    gid: "aws_sdk_transfer.types.posix_id.PosixId"
    """<p>The POSIX group ID used for all EFS operations by this user.</p>"""
    secondary_gids: NotRequired["aws_sdk_transfer.types.secondary_gids.SecondaryGids"]
    """<p>The secondary POSIX group IDs used for all EFS operations by this user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PosixProfile) -> dict:
    out: dict = {}
    out["Uid"] = value["uid"]
    out["Gid"] = value["gid"]
    if "secondary_gids" in value:
        import aws_sdk_transfer.types.secondary_gids

        out["SecondaryGids"] = (
            aws_sdk_transfer.types.secondary_gids.serialize_aws_json_1_1(
                value["secondary_gids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PosixProfile:
    out: PosixProfile = {}  # type: ignore[typeddict-item]
    if "Uid" in data:
        out["uid"] = data["Uid"]
    else:
        raise DeserializationError("PosixProfile.uid required")
    if "Gid" in data:
        out["gid"] = data["Gid"]
    else:
        raise DeserializationError("PosixProfile.gid required")
    if "SecondaryGids" in data:
        import aws_sdk_transfer.types.secondary_gids

        out["secondary_gids"] = (
            aws_sdk_transfer.types.secondary_gids.deserialize_aws_json_1_1(
                data["SecondaryGids"]
            )
        )
    return out
