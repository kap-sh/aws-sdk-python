"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#State``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""State"""
State: TypeAlias = Literal[
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


def serialize_json(value: State) -> str:
    return value


def deserialize_json(data: str) -> State:
    if data not in _VALUES:
        raise DeserializationError(f"unknown State value: {data!r}")
    return cast(State, data)
