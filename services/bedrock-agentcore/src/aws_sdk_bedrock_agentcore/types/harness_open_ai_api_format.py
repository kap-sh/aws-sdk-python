"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessOpenAiApiFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

HarnessOpenAiApiFormat: TypeAlias = Literal[
    "chat_completions",
    "responses",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "chat_completions",
        "responses",
    )
)


def serialize_json(value: HarnessOpenAiApiFormat) -> str:
    return value


def deserialize_json(data: str) -> HarnessOpenAiApiFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessOpenAiApiFormat value: {data!r}")
    return cast(HarnessOpenAiApiFormat, data)
