"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailTemplateMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.email_template_metadata

EmailTemplateMetadataList: TypeAlias = list[
    "capo_sesv2.types.email_template_metadata.EmailTemplateMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailTemplateMetadataList) -> list:
    import capo_sesv2.types.email_template_metadata

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.email_template_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailTemplateMetadataList:
    import capo_sesv2.types.email_template_metadata

    out: EmailTemplateMetadataList = []
    for item in data:
        out.append(capo_sesv2.types.email_template_metadata.deserialize_json(item))
    return out
