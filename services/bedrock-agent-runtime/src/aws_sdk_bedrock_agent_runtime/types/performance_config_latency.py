"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PerformanceConfigLatency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

PerformanceConfigLatency: TypeAlias = Literal[
    "standard",
    "optimized",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "optimized",
    )
)


def serialize_json(value: PerformanceConfigLatency) -> str:
    return value


def deserialize_json(data: str) -> PerformanceConfigLatency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PerformanceConfigLatency value: {data!r}")
    return cast(PerformanceConfigLatency, data)
