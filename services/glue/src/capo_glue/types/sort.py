"""Generated from Smithy shape ``com.amazonaws.glue#Sort``."""

from typing import Literal, TypeAlias, cast

Sort: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sort) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Sort:
    return cast(Sort, data)
