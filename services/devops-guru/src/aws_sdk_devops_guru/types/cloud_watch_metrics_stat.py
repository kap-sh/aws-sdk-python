"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricsStat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Sum",
        "Average",
        "SampleCount",
        "Minimum",
        "Maximum",
        "p99",
        "p90",
        "p50",
    )
)


def serialize_json(value: CloudWatchMetricsStat) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchMetricsStat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloudWatchMetricsStat value: {data!r}")
    return cast(CloudWatchMetricsStat, data)
