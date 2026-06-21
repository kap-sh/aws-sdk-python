"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsType``."""

from typing import Literal, TypeAlias, cast

ColumnStatisticsType: TypeAlias = Literal[
    "BOOLEAN",
    "DATE",
    "DECIMAL",
    "DOUBLE",
    "LONG",
    "STRING",
    "BINARY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ColumnStatisticsType:
    return cast(ColumnStatisticsType, data)
