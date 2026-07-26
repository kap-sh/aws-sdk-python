"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsMetric``."""

from typing import Literal, TypeAlias, cast

WorkloadInsightsMetric: TypeAlias = Literal[
    "TIMEOUTS",
    "RETRANSMISSIONS",
    "DATA_TRANSFERRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadInsightsMetric) -> str:
    return value


def deserialize_json(data: str) -> WorkloadInsightsMetric:
    return cast(WorkloadInsightsMetric, data)
