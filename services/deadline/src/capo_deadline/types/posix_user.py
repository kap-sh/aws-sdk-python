"""Generated from Smithy shape ``com.amazonaws.deadline#PosixUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.string


class PosixUser(TypedDict, closed=True):
    user: "capo_deadline.types.string.String"
    """<p>The name of the POSIX user.</p>"""
    group: "capo_deadline.types.string.String"
    """<p>The name of the POSIX user's group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PosixUser) -> dict:
    out: dict = {}
    out["user"] = value["user"]
    out["group"] = value["group"]
    return out


def deserialize_json(data: dict) -> PosixUser:
    out: PosixUser = {}  # type: ignore[typeddict-item]
    if "user" in data:
        out["user"] = data["user"]
    else:
        raise DeserializationError("PosixUser.user required")
    if "group" in data:
        out["group"] = data["group"]
    else:
        raise DeserializationError("PosixUser.group required")
    return out
