"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorMetric``."""

from typing import Literal, TypeAlias, cast

MonitorMetric: TypeAlias = Literal[
    "ROUND_TRIP_TIME",
    "TIMEOUTS",
    "RETRANSMISSIONS",
    "DATA_TRANSFERRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorMetric) -> str:
    return value


def deserialize_json(data: str) -> MonitorMetric:
    return cast(MonitorMetric, data)
