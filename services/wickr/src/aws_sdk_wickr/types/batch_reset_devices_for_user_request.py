"""Generated from Smithy shape ``com.amazonaws.wickr#BatchResetDevicesForUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.app_ids
    import aws_sdk_wickr.types.client_token
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.user_id


class BatchResetDevicesForUserRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the user whose devices will be reset.</p>"""
    user_id: "aws_sdk_wickr.types.user_id.UserId"
    """<p>The ID of the user whose devices will be reset.</p>"""
    app_ids: "aws_sdk_wickr.types.app_ids.AppIds"
    """<p>A list of application IDs identifying the specific devices to be reset for the user. Maximum 50 devices per batch request.</p>"""
    client_token: NotRequired["aws_sdk_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchResetDevicesForUserRequest) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.app_ids

    out["appIds"] = aws_sdk_wickr.types.app_ids.serialize_json(value["app_ids"])
    return out


def deserialize_json(data: dict) -> BatchResetDevicesForUserRequest:
    out: BatchResetDevicesForUserRequest = {}  # type: ignore[typeddict-item]
    if "appIds" in data:
        import aws_sdk_wickr.types.app_ids

        out["app_ids"] = aws_sdk_wickr.types.app_ids.deserialize_json(data["appIds"])
    else:
        raise DeserializationError("BatchResetDevicesForUserRequest.app_ids required")
    return out
