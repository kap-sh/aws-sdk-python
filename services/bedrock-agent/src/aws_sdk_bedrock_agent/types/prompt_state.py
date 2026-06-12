"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

PromptState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: PromptState) -> str:
    return value


def deserialize_json(data: str) -> PromptState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromptState value: {data!r}")
    return cast(PromptState, data)
