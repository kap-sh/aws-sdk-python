"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteEmailTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.message_body


class DeleteEmailTemplateResponse(TypedDict):
    message_body: NotRequired["aws_sdk_pinpoint.types.message_body.MessageBody"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailTemplateResponse) -> dict:
    out: dict = {}
    if "message_body" in value:
        import aws_sdk_pinpoint.types.message_body

        out["MessageBody"] = aws_sdk_pinpoint.types.message_body.serialize_json(
            value["message_body"]
        )
    return out


def deserialize_json(data: dict) -> DeleteEmailTemplateResponse:
    out: DeleteEmailTemplateResponse = {}  # type: ignore[typeddict-item]
    if "MessageBody" in data:
        import aws_sdk_pinpoint.types.message_body

        out["message_body"] = aws_sdk_pinpoint.types.message_body.deserialize_json(
            data["MessageBody"]
        )
    return out
