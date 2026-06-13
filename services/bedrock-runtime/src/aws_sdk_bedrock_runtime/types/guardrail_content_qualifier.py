"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentQualifier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailContentQualifier: TypeAlias = Literal[
    "grounding_source",
    "query",
    "guard_content",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "grounding_source",
        "query",
        "guard_content",
    )
)


def serialize_json(value: GuardrailContentQualifier) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentQualifier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailContentQualifier value: {data!r}")
    return cast(GuardrailContentQualifier, data)
