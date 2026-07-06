"""Generated from Smithy shape ``com.amazonaws.wickr#BlockedGuestUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class BlockedGuestUser(TypedDict, closed=True):
    username: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The username of the blocked guest user.</p>"""
    admin: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The username of the administrator who blocked this guest user.</p>"""
    modified: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The timestamp when the guest user was blocked or last modified.</p>"""
    username_hash: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The unique username hash identifier for the blocked guest user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockedGuestUser) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["admin"] = value["admin"]
    out["modified"] = value["modified"]
    out["usernameHash"] = value["username_hash"]
    return out


def deserialize_json(data: dict) -> BlockedGuestUser:
    out: BlockedGuestUser = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    else:
        raise DeserializationError("BlockedGuestUser.username required")
    if "admin" in data:
        out["admin"] = data["admin"]
    else:
        raise DeserializationError("BlockedGuestUser.admin required")
    if "modified" in data:
        out["modified"] = data["modified"]
    else:
        raise DeserializationError("BlockedGuestUser.modified required")
    if "usernameHash" in data:
        out["username_hash"] = data["usernameHash"]
    else:
        raise DeserializationError("BlockedGuestUser.username_hash required")
    return out
