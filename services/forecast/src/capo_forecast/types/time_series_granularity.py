"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesGranularity``."""

from typing import Literal, TypeAlias, cast

TimeSeriesGranularity: TypeAlias = Literal[
    "ALL",
    "SPECIFIC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesGranularity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeSeriesGranularity:
    return cast(TimeSeriesGranularity, data)
