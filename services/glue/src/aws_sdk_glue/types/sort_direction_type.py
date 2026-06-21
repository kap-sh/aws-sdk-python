"""Generated from Smithy shape ``com.amazonaws.glue#SortDirectionType``."""

from typing import Literal, TypeAlias, cast

SortDirectionType: TypeAlias = Literal[
    "DESCENDING",
    "ASCENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortDirectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortDirectionType:
    return cast(SortDirectionType, data)
