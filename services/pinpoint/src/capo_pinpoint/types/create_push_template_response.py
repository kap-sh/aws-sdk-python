"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreatePushTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.create_template_message_body


class CreatePushTemplateResponse(TypedDict, closed=True):
    create_template_message_body: NotRequired[
        "capo_pinpoint.types.create_template_message_body.CreateTemplateMessageBody"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreatePushTemplateResponse) -> dict:
    out: dict = {}
    if "create_template_message_body" in value:
        import capo_pinpoint.types.create_template_message_body

        out["CreateTemplateMessageBody"] = (
            capo_pinpoint.types.create_template_message_body.serialize_json(
                value["create_template_message_body"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreatePushTemplateResponse:
    out: CreatePushTemplateResponse = {}  # type: ignore[typeddict-item]
    if "CreateTemplateMessageBody" in data:
        import capo_pinpoint.types.create_template_message_body

        out["create_template_message_body"] = (
            capo_pinpoint.types.create_template_message_body.deserialize_json(
                data["CreateTemplateMessageBody"]
            )
        )
    return out
