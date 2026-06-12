"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppMessageTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.meta_template_definition


class CreateWhatsAppMessageTemplateInput(TypedDict):
    template_definition: (
        "aws_sdk_socialmessaging.types.meta_template_definition.MetaTemplateDefinition"
    )
    """<p>The complete template definition as a JSON blob.</p>"""
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account to associate with this template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppMessageTemplateInput) -> dict:
    out: dict = {}
    import aws_sdk_socialmessaging.types.meta_template_definition

    out["templateDefinition"] = (
        aws_sdk_socialmessaging.types.meta_template_definition.serialize_json(
            value["template_definition"]
        )
    )
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateWhatsAppMessageTemplateInput:
    out: CreateWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
    if "templateDefinition" in data:
        import aws_sdk_socialmessaging.types.meta_template_definition

        out["template_definition"] = (
            aws_sdk_socialmessaging.types.meta_template_definition.deserialize_json(
                data["templateDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWhatsAppMessageTemplateInput.template_definition required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateWhatsAppMessageTemplateInput.id required")
    return out
