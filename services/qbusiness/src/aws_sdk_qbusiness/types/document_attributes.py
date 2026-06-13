"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_attribute

DocumentAttributes: TypeAlias = list[
    "aws_sdk_qbusiness.types.document_attribute.DocumentAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributes) -> list:
    import aws_sdk_qbusiness.types.document_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.document_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentAttributes:
    import aws_sdk_qbusiness.types.document_attribute

    out: DocumentAttributes = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.document_attribute.deserialize_json(item))
    return out
