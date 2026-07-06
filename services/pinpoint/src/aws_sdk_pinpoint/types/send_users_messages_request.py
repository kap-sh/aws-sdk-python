"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendUsersMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.send_users_message_request


class SendUsersMessagesRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    send_users_message_request: NotRequired[
        "aws_sdk_pinpoint.types.send_users_message_request.SendUsersMessageRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SendUsersMessagesRequest) -> dict:
    out: dict = {}
    if "send_users_message_request" in value:
        import aws_sdk_pinpoint.types.send_users_message_request

        out["SendUsersMessageRequest"] = (
            aws_sdk_pinpoint.types.send_users_message_request.serialize_json(
                value["send_users_message_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendUsersMessagesRequest:
    out: SendUsersMessagesRequest = {}  # type: ignore[typeddict-item]
    if "SendUsersMessageRequest" in data:
        import aws_sdk_pinpoint.types.send_users_message_request

        out["send_users_message_request"] = (
            aws_sdk_pinpoint.types.send_users_message_request.deserialize_json(
                data["SendUsersMessageRequest"]
            )
        )
    return out
