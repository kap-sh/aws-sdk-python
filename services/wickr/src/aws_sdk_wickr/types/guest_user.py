"""Generated from Smithy shape ``com.amazonaws.wickr#GuestUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class GuestUser(TypedDict, closed=True):
    billing_period: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The billing period when this guest user accessed the network (e.g., '2024-01').</p>"""
    username: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The username of the guest user.</p>"""
    username_hash: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The unique username hash identifier for the guest user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuestUser) -> dict:
    out: dict = {}
    out["billingPeriod"] = value["billing_period"]
    out["username"] = value["username"]
    out["usernameHash"] = value["username_hash"]
    return out


def deserialize_json(data: dict) -> GuestUser:
    out: GuestUser = {}  # type: ignore[typeddict-item]
    if "billingPeriod" in data:
        out["billing_period"] = data["billingPeriod"]
    else:
        raise DeserializationError("GuestUser.billing_period required")
    if "username" in data:
        out["username"] = data["username"]
    else:
        raise DeserializationError("GuestUser.username required")
    if "usernameHash" in data:
        out["username_hash"] = data["usernameHash"]
    else:
        raise DeserializationError("GuestUser.username_hash required")
    return out
