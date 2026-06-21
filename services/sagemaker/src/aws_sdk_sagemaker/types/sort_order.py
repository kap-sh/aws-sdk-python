"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortOrder``."""

from typing import Literal, TypeAlias, cast

SortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortOrder:
    return cast(SortOrder, data)
