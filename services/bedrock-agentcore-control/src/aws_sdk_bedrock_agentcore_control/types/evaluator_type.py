"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

EvaluatorType: TypeAlias = Literal[
    "Builtin",
    "Custom",
    "CustomCode",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Builtin",
        "Custom",
        "CustomCode",
    )
)


def serialize_json(value: EvaluatorType) -> str:
    return value


def deserialize_json(data: str) -> EvaluatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluatorType value: {data!r}")
    return cast(EvaluatorType, data)
