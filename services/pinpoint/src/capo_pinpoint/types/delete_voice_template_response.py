"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteVoiceTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.message_body


class DeleteVoiceTemplateResponse(TypedDict, closed=True):
    message_body: NotRequired["capo_pinpoint.types.message_body.MessageBody"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVoiceTemplateResponse) -> dict:
    out: dict = {}
    if "message_body" in value:
        import capo_pinpoint.types.message_body

        out["MessageBody"] = capo_pinpoint.types.message_body.serialize_json(
            value["message_body"]
        )
    return out


def deserialize_json(data: dict) -> DeleteVoiceTemplateResponse:
    out: DeleteVoiceTemplateResponse = {}  # type: ignore[typeddict-item]
    if "MessageBody" in data:
        import capo_pinpoint.types.message_body

        out["message_body"] = capo_pinpoint.types.message_body.deserialize_json(
            data["MessageBody"]
        )
    return out
