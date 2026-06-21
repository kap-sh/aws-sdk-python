"""Generated from Smithy shape ``com.amazonaws.forecast#AttributeType``."""

from typing import Literal, TypeAlias, cast

AttributeType: TypeAlias = Literal[
    "string",
    "integer",
    "float",
    "timestamp",
    "geolocation",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttributeType:
    return cast(AttributeType, data)
