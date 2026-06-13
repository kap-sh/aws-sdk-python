"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckLogicWarningType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AutomatedReasoningCheckLogicWarningType: TypeAlias = Literal[
    "ALWAYS_TRUE",
    "ALWAYS_FALSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS_TRUE",
        "ALWAYS_FALSE",
    )
)


def serialize_json(value: AutomatedReasoningCheckLogicWarningType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningCheckLogicWarningType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningCheckLogicWarningType value: {data!r}"
        )
    return cast(AutomatedReasoningCheckLogicWarningType, data)
