"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessageListType``."""

from typing import Literal, TypeAlias, cast

StructuredMessageListType: TypeAlias = Literal[
    "FIXED_CAPACITY",
    "DYNAMIC_UNBOUNDED_CAPACITY",
    "DYNAMIC_BOUNDED_CAPACITY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredMessageListType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StructuredMessageListType:
    return cast(StructuredMessageListType, data)
