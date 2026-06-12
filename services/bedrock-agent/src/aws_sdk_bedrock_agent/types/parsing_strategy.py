"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ParsingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ParsingStrategy: TypeAlias = Literal[
    "BEDROCK_FOUNDATION_MODEL",
    "BEDROCK_DATA_AUTOMATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEDROCK_FOUNDATION_MODEL",
        "BEDROCK_DATA_AUTOMATION",
    )
)


def serialize_json(value: ParsingStrategy) -> str:
    return value


def deserialize_json(data: str) -> ParsingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParsingStrategy value: {data!r}")
    return cast(ParsingStrategy, data)
