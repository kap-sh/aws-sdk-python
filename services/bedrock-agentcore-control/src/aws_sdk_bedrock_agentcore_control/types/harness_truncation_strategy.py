"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTruncationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

HarnessTruncationStrategy: TypeAlias = Literal[
    "sliding_window",
    "summarization",
    "none",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sliding_window",
        "summarization",
        "none",
    )
)


def serialize_json(value: HarnessTruncationStrategy) -> str:
    return value


def deserialize_json(data: str) -> HarnessTruncationStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessTruncationStrategy value: {data!r}")
    return cast(HarnessTruncationStrategy, data)
