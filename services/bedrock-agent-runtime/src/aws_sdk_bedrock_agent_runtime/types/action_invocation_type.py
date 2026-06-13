"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionInvocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

ActionInvocationType: TypeAlias = Literal[
    "RESULT",
    "USER_CONFIRMATION",
    "USER_CONFIRMATION_AND_RESULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESULT",
        "USER_CONFIRMATION",
        "USER_CONFIRMATION_AND_RESULT",
    )
)


def serialize_json(value: ActionInvocationType) -> str:
    return value


def deserialize_json(data: str) -> ActionInvocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionInvocationType value: {data!r}")
    return cast(ActionInvocationType, data)
