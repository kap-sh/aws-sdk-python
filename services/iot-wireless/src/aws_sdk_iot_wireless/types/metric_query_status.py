"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryStatus``."""

from typing import Literal, TypeAlias, cast

MetricQueryStatus: TypeAlias = Literal[
    "Succeeded",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryStatus) -> str:
    return value


def deserialize_json(data: str) -> MetricQueryStatus:
    return cast(MetricQueryStatus, data)
