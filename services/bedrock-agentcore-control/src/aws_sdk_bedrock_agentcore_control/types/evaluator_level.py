"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

EvaluatorLevel: TypeAlias = Literal[
    "TOOL_CALL",
    "TRACE",
    "SESSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOOL_CALL",
        "TRACE",
        "SESSION",
    )
)


def serialize_json(value: EvaluatorLevel) -> str:
    return value


def deserialize_json(data: str) -> EvaluatorLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluatorLevel value: {data!r}")
    return cast(EvaluatorLevel, data)
