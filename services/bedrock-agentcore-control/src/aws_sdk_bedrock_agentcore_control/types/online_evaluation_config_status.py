"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnlineEvaluationConfigStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

OnlineEvaluationConfigStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
        "CREATE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "DELETING",
        "ERROR",
    )
)


def serialize_json(value: OnlineEvaluationConfigStatus) -> str:
    return value


def deserialize_json(data: str) -> OnlineEvaluationConfigStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OnlineEvaluationConfigStatus value: {data!r}"
        )
    return cast(OnlineEvaluationConfigStatus, data)
