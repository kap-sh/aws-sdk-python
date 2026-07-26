"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsState``."""

from typing import Literal, TypeAlias, cast

ColumnStatisticsState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ColumnStatisticsState:
    return cast(ColumnStatisticsState, data)
