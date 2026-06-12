"""Generated from Smithy shape ``com.amazonaws.wickr#BatchDeleteUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.client_token
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.user_ids


class BatchDeleteUserRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which users will be deleted.</p>"""
    user_ids: "aws_sdk_wickr.types.user_ids.UserIds"
    """<p>A list of user IDs identifying the users to be deleted from the network. Maximum 50 users per batch request.</p>"""
    client_token: NotRequired["aws_sdk_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without attempting to delete users again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteUserRequest) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.user_ids

    out["userIds"] = aws_sdk_wickr.types.user_ids.serialize_json(value["user_ids"])
    return out


def deserialize_json(data: dict) -> BatchDeleteUserRequest:
    out: BatchDeleteUserRequest = {}  # type: ignore[typeddict-item]
    if "userIds" in data:
        import aws_sdk_wickr.types.user_ids

        out["user_ids"] = aws_sdk_wickr.types.user_ids.deserialize_json(data["userIds"])
    else:
        raise DeserializationError("BatchDeleteUserRequest.user_ids required")
    return out
