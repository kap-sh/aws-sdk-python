"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnlineEvaluationExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

OnlineEvaluationExecutionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: OnlineEvaluationExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> OnlineEvaluationExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OnlineEvaluationExecutionStatus value: {data!r}"
        )
    return cast(OnlineEvaluationExecutionStatus, data)
