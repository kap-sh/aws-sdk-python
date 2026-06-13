"""Generated from Smithy shape ``com.amazonaws.datazone#UserDetails``."""

from typing import TypedDict
from aws_sdk_datazone.errors import DeserializationError


class UserDetails(TypedDict):
    user_id: "str"
    """<p>The identifier of the Amazon DataZone user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserDetails) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> UserDetails:
    out: UserDetails = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UserDetails.user_id required")
    return out
