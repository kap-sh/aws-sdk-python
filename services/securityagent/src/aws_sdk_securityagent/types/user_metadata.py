"""Generated from Smithy shape ``com.amazonaws.securityagent#UserMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.sensitive_email


class UserMetadata(TypedDict, closed=True):
    username: "str"
    """<p>The username of the user.</p>"""
    email: "aws_sdk_securityagent.types.sensitive_email.SensitiveEmail"
    """<p>The email address of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserMetadata) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> UserMetadata:
    out: UserMetadata = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    else:
        raise DeserializationError("UserMetadata.username required")
    if "email" in data:
        out["email"] = data["email"]
    else:
        raise DeserializationError("UserMetadata.email required")
    return out
