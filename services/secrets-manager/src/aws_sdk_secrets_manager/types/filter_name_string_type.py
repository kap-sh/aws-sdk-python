"""Generated from Smithy shape ``com.amazonaws.secretsmanager#FilterNameStringType``."""

from typing import Literal, TypeAlias, cast

FilterNameStringType: TypeAlias = Literal[
    "description",
    "name",
    "tag-key",
    "tag-value",
    "primary-region",
    "owning-service",
    "all",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterNameStringType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterNameStringType:
    return cast(FilterNameStringType, data)
