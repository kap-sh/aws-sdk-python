"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SortOrderType``."""

from typing import Literal, TypeAlias, cast

SortOrderType: TypeAlias = Literal[
    "asc",
    "desc",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortOrderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortOrderType:
    return cast(SortOrderType, data)
