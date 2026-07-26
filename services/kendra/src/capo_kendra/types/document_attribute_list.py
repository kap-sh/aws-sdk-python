"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute

DocumentAttributeList: TypeAlias = list[
    "capo_kendra.types.document_attribute.DocumentAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeList) -> list:
    import capo_kendra.types.document_attribute

    out: list = []
    for item in value:
        out.append(capo_kendra.types.document_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentAttributeList:
    import capo_kendra.types.document_attribute

    out: DocumentAttributeList = []
    for item in data:
        out.append(capo_kendra.types.document_attribute.deserialize_aws_json_1_1(item))
    return out
