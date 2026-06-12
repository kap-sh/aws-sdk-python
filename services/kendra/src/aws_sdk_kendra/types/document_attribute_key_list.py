"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_key

DocumentAttributeKeyList: TypeAlias = list[
    "aws_sdk_kendra.types.document_attribute_key.DocumentAttributeKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DocumentAttributeKeyList:
    return list(data)
