"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.message_response


class SendMessagesResponse(TypedDict, closed=True):
    message_response: NotRequired[
        "aws_sdk_pinpoint.types.message_response.MessageResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SendMessagesResponse) -> dict:
    out: dict = {}
    if "message_response" in value:
        import aws_sdk_pinpoint.types.message_response

        out["MessageResponse"] = aws_sdk_pinpoint.types.message_response.serialize_json(
            value["message_response"]
        )
    return out


def deserialize_json(data: dict) -> SendMessagesResponse:
    out: SendMessagesResponse = {}  # type: ignore[typeddict-item]
    if "MessageResponse" in data:
        import aws_sdk_pinpoint.types.message_response

        out["message_response"] = (
            aws_sdk_pinpoint.types.message_response.deserialize_json(
                data["MessageResponse"]
            )
        )
    return out
