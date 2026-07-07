"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.message_request


class SendMessagesRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    message_request: NotRequired[
        "aws_sdk_pinpoint.types.message_request.MessageRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SendMessagesRequest) -> dict:
    out: dict = {}
    if "message_request" in value:
        import aws_sdk_pinpoint.types.message_request

        out["MessageRequest"] = aws_sdk_pinpoint.types.message_request.serialize_json(
            value["message_request"]
        )
    return out


def deserialize_json(data: dict) -> SendMessagesRequest:
    out: SendMessagesRequest = {}  # type: ignore[typeddict-item]
    if "MessageRequest" in data:
        import aws_sdk_pinpoint.types.message_request

        out["message_request"] = (
            aws_sdk_pinpoint.types.message_request.deserialize_json(
                data["MessageRequest"]
            )
        )
    return out
