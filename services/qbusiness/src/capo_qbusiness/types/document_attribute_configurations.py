"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_configuration

DocumentAttributeConfigurations: TypeAlias = list[
    "capo_qbusiness.types.document_attribute_configuration.DocumentAttributeConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeConfigurations) -> list:
    import capo_qbusiness.types.document_attribute_configuration

    out: list = []
    for item in value:
        out.append(
            capo_qbusiness.types.document_attribute_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DocumentAttributeConfigurations:
    import capo_qbusiness.types.document_attribute_configuration

    out: DocumentAttributeConfigurations = []
    for item in data:
        out.append(
            capo_qbusiness.types.document_attribute_configuration.deserialize_json(item)
        )
    return out
