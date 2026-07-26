"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PerformanceConfigLatency``."""

from typing import Literal, TypeAlias, cast

PerformanceConfigLatency: TypeAlias = Literal[
    "standard",
    "optimized",
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceConfigLatency) -> str:
    return value


def deserialize_json(data: str) -> PerformanceConfigLatency:
    return cast(PerformanceConfigLatency, data)
