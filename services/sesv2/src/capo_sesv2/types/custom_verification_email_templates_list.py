"""Generated from Smithy shape ``com.amazonaws.sesv2#CustomVerificationEmailTemplatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.custom_verification_email_template_metadata

CustomVerificationEmailTemplatesList: TypeAlias = list[
    "capo_sesv2.types.custom_verification_email_template_metadata.CustomVerificationEmailTemplateMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomVerificationEmailTemplatesList) -> list:
    import capo_sesv2.types.custom_verification_email_template_metadata

    out: list = []
    for item in value:
        out.append(
            capo_sesv2.types.custom_verification_email_template_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CustomVerificationEmailTemplatesList:
    import capo_sesv2.types.custom_verification_email_template_metadata

    out: CustomVerificationEmailTemplatesList = []
    for item in data:
        out.append(
            capo_sesv2.types.custom_verification_email_template_metadata.deserialize_json(
                item
            )
        )
    return out
