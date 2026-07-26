"""Generated from Smithy shape ``com.amazonaws.efs#PosixUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_efs.types.gid
    import capo_efs.types.secondary_gids
    import capo_efs.types.uid


class PosixUser(TypedDict, closed=True):
    uid: "capo_efs.types.uid.Uid"
    """<p>The POSIX user ID used for all file system operations using this access point.</p>"""
    gid: "capo_efs.types.gid.Gid"
    """<p>The POSIX group ID used for all file system operations using this access point.</p>"""
    secondary_gids: NotRequired["capo_efs.types.secondary_gids.SecondaryGids"]
    """<p>Secondary POSIX group IDs used for all file system operations using this access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PosixUser) -> dict:
    out: dict = {}
    out["Uid"] = value["uid"]
    out["Gid"] = value["gid"]
    if "secondary_gids" in value:
        import capo_efs.types.secondary_gids

        out["SecondaryGids"] = capo_efs.types.secondary_gids.serialize_json(
            value["secondary_gids"]
        )
    return out


def deserialize_json(data: dict) -> PosixUser:
    out: PosixUser = {}  # type: ignore[typeddict-item]
    if "Uid" in data:
        out["uid"] = data["Uid"]
    else:
        raise DeserializationError("PosixUser.uid required")
    if "Gid" in data:
        out["gid"] = data["Gid"]
    else:
        raise DeserializationError("PosixUser.gid required")
    if "SecondaryGids" in data:
        import capo_efs.types.secondary_gids

        out["secondary_gids"] = capo_efs.types.secondary_gids.deserialize_json(
            data["SecondaryGids"]
        )
    return out
