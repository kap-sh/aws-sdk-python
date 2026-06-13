"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsMetric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkflowmonitor.errors import DeserializationError

WorkloadInsightsMetric: TypeAlias = Literal[
    "TIMEOUTS",
    "RETRANSMISSIONS",
    "DATA_TRANSFERRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TIMEOUTS",
        "RETRANSMISSIONS",
        "DATA_TRANSFERRED",
    )
)


def serialize_json(value: WorkloadInsightsMetric) -> str:
    return value


def deserialize_json(data: str) -> WorkloadInsightsMetric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkloadInsightsMetric value: {data!r}")
    return cast(WorkloadInsightsMetric, data)
