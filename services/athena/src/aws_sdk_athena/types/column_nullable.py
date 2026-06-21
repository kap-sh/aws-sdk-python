"""Generated from Smithy shape ``com.amazonaws.athena#ColumnNullable``."""

from typing import Literal, TypeAlias, cast

ColumnNullable: TypeAlias = Literal[
    "NOT_NULL",
    "NULLABLE",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnNullable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ColumnNullable:
    return cast(ColumnNullable, data)
