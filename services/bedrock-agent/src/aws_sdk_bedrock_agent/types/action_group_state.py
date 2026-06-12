"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ActionGroupState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ActionGroupState: TypeAlias = Literal[
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


def serialize_json(value: ActionGroupState) -> str:
    return value


def deserialize_json(data: str) -> ActionGroupState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionGroupState value: {data!r}")
    return cast(ActionGroupState, data)
