"""Generated from Smithy shape ``com.amazonaws.dynamodb#Select``."""

from typing import Literal, TypeAlias, cast

Select: TypeAlias = Literal[
    "ALL_ATTRIBUTES",
    "ALL_PROJECTED_ATTRIBUTES",
    "SPECIFIC_ATTRIBUTES",
    "COUNT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Select) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Select:
    return cast(Select, data)
