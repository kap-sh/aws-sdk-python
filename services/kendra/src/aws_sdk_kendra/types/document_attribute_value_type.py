"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeValueType``."""

from typing import Literal, TypeAlias, cast

DocumentAttributeValueType: TypeAlias = Literal[
    "STRING_VALUE",
    "STRING_LIST_VALUE",
    "LONG_VALUE",
    "DATE_VALUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentAttributeValueType:
    return cast(DocumentAttributeValueType, data)
