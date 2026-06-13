"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ConfirmationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

ConfirmationState: TypeAlias = Literal[
    "CONFIRM",
    "DENY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFIRM",
        "DENY",
    )
)


def serialize_json(value: ConfirmationState) -> str:
    return value


def deserialize_json(data: str) -> ConfirmationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfirmationState value: {data!r}")
    return cast(ConfirmationState, data)
