"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdatePushTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.message_body


class UpdatePushTemplateResponse(TypedDict, closed=True):
    message_body: NotRequired["aws_sdk_pinpoint.types.message_body.MessageBody"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePushTemplateResponse) -> dict:
    out: dict = {}
    if "message_body" in value:
        import aws_sdk_pinpoint.types.message_body

        out["MessageBody"] = aws_sdk_pinpoint.types.message_body.serialize_json(
            value["message_body"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePushTemplateResponse:
    out: UpdatePushTemplateResponse = {}  # type: ignore[typeddict-item]
    if "MessageBody" in data:
        import aws_sdk_pinpoint.types.message_body

        out["message_body"] = aws_sdk_pinpoint.types.message_body.deserialize_json(
            data["MessageBody"]
        )
    return out
