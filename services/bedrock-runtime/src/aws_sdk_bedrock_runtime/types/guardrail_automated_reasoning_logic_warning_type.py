"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningLogicWarningType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailAutomatedReasoningLogicWarningType: TypeAlias = Literal[
    "ALWAYS_FALSE",
    "ALWAYS_TRUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS_FALSE",
        "ALWAYS_TRUE",
    )
)


def serialize_json(value: GuardrailAutomatedReasoningLogicWarningType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailAutomatedReasoningLogicWarningType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailAutomatedReasoningLogicWarningType value: {data!r}"
        )
    return cast(GuardrailAutomatedReasoningLogicWarningType, data)
