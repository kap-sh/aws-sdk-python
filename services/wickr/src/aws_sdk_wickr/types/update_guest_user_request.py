"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateGuestUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id


class UpdateGuestUserRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where the guest user's status will be updated.</p>"""
    username_hash: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The username hash (unique identifier) of the guest user to update.</p>"""
    block: "bool"
    """<p>Set to true to block the guest user or false to unblock them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGuestUserRequest) -> dict:
    out: dict = {}
    out["block"] = value["block"]
    return out


def deserialize_json(data: dict) -> UpdateGuestUserRequest:
    out: UpdateGuestUserRequest = {}  # type: ignore[typeddict-item]
    if "block" in data:
        out["block"] = data["block"]
    else:
        raise DeserializationError("UpdateGuestUserRequest.block required")
    return out
