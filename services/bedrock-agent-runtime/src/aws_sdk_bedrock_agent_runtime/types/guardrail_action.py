"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuardrailAction: TypeAlias = Literal[
    "INTERVENED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERVENED",
        "NONE",
    )
)


def serialize_json(value: GuardrailAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailAction value: {data!r}")
    return cast(GuardrailAction, data)
