"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute

DocumentAttributes: TypeAlias = list[
    "capo_qbusiness.types.document_attribute.DocumentAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributes) -> list:
    import capo_qbusiness.types.document_attribute

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.document_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentAttributes:
    import capo_qbusiness.types.document_attribute

    out: DocumentAttributes = []
    for item in data:
        out.append(capo_qbusiness.types.document_attribute.deserialize_json(item))
    return out
