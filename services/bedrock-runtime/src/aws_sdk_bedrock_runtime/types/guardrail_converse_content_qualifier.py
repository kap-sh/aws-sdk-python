"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseContentQualifier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailConverseContentQualifier: TypeAlias = Literal[
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


def serialize_json(value: GuardrailConverseContentQualifier) -> str:
    return value


def deserialize_json(data: str) -> GuardrailConverseContentQualifier:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailConverseContentQualifier value: {data!r}"
        )
    return cast(GuardrailConverseContentQualifier, data)
