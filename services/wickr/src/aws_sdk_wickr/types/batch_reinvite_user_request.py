"""Generated from Smithy shape ``com.amazonaws.wickr#BatchReinviteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.client_token
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.user_ids


class BatchReinviteUserRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where users will be reinvited.</p>"""
    user_ids: "aws_sdk_wickr.types.user_ids.UserIds"
    """<p>A list of user IDs identifying the users to be reinvited to the network. Maximum 50 users per batch request.</p>"""
    client_token: NotRequired["aws_sdk_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReinviteUserRequest) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.user_ids

    out["userIds"] = aws_sdk_wickr.types.user_ids.serialize_json(value["user_ids"])
    return out


def deserialize_json(data: dict) -> BatchReinviteUserRequest:
    out: BatchReinviteUserRequest = {}  # type: ignore[typeddict-item]
    if "userIds" in data:
        import aws_sdk_wickr.types.user_ids

        out["user_ids"] = aws_sdk_wickr.types.user_ids.deserialize_json(data["userIds"])
    else:
        raise DeserializationError("BatchReinviteUserRequest.user_ids required")
    return out
