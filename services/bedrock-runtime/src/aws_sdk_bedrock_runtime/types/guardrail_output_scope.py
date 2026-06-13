"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOutputScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailOutputScope: TypeAlias = Literal[
    "INTERVENTIONS",
    "FULL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERVENTIONS",
        "FULL",
    )
)


def serialize_json(value: GuardrailOutputScope) -> str:
    return value


def deserialize_json(data: str) -> GuardrailOutputScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailOutputScope value: {data!r}")
    return cast(GuardrailOutputScope, data)
