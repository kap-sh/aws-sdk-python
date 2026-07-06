"""Generated from Smithy shape ``com.amazonaws.wickr#BatchCreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.batch_create_user_request_items
    import aws_sdk_wickr.types.client_token
    import aws_sdk_wickr.types.network_id


class BatchCreateUserRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where users will be created.</p>"""
    users: "aws_sdk_wickr.types.batch_create_user_request_items.BatchCreateUserRequestItems"
    """<p>A list of user objects containing the details for each user to be created, including username, name, security groups, and optional invite codes. Maximum 50 users per batch request.</p>"""
    client_token: NotRequired["aws_sdk_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without creating duplicate users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateUserRequest) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.batch_create_user_request_items

    out["users"] = aws_sdk_wickr.types.batch_create_user_request_items.serialize_json(
        value["users"]
    )
    return out


def deserialize_json(data: dict) -> BatchCreateUserRequest:
    out: BatchCreateUserRequest = {}  # type: ignore[typeddict-item]
    if "users" in data:
        import aws_sdk_wickr.types.batch_create_user_request_items

        out["users"] = (
            aws_sdk_wickr.types.batch_create_user_request_items.deserialize_json(
                data["users"]
            )
        )
    else:
        raise DeserializationError("BatchCreateUserRequest.users required")
    return out
