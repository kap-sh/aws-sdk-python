"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailContentSource: TypeAlias = Literal[
    "INPUT",
    "OUTPUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INPUT",
        "OUTPUT",
    )
)


def serialize_json(value: GuardrailContentSource) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailContentSource value: {data!r}")
    return cast(GuardrailContentSource, data)
