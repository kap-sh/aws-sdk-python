"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AttributeDataType``."""

from typing import Literal, TypeAlias, cast

AttributeDataType: TypeAlias = Literal[
    "String",
    "Number",
    "DateTime",
    "Boolean",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttributeDataType:
    return cast(AttributeDataType, data)
