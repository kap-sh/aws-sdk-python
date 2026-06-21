"""Generated from Smithy shape ``com.amazonaws.cloudtrail#SourceEventCategory``."""

from typing import Literal, TypeAlias, cast

SourceEventCategory: TypeAlias = Literal[
    "Management",
    "Data",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceEventCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceEventCategory:
    return cast(SourceEventCategory, data)
