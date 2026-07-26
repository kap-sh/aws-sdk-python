"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateInAppTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.template_create_message_body


class CreateInAppTemplateResponse(TypedDict, closed=True):
    template_create_message_body: NotRequired[
        "capo_pinpoint.types.template_create_message_body.TemplateCreateMessageBody"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateInAppTemplateResponse) -> dict:
    out: dict = {}
    if "template_create_message_body" in value:
        import capo_pinpoint.types.template_create_message_body

        out["TemplateCreateMessageBody"] = (
            capo_pinpoint.types.template_create_message_body.serialize_json(
                value["template_create_message_body"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateInAppTemplateResponse:
    out: CreateInAppTemplateResponse = {}  # type: ignore[typeddict-item]
    if "TemplateCreateMessageBody" in data:
        import capo_pinpoint.types.template_create_message_body

        out["template_create_message_body"] = (
            capo_pinpoint.types.template_create_message_body.deserialize_json(
                data["TemplateCreateMessageBody"]
            )
        )
    return out
