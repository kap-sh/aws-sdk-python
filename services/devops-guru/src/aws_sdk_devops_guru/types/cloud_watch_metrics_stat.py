"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricsStat``."""

from typing import Literal, TypeAlias, cast

CloudWatchMetricsStat: TypeAlias = Literal[
    "Sum",
    "Average",
    "SampleCount",
    "Minimum",
    "Maximum",
    "p99",
    "p90",
    "p50",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMetricsStat) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchMetricsStat:
    return cast(CloudWatchMetricsStat, data)
