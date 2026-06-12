"""Generated from Smithy shape ``com.amazonaws.iot#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ActionType: TypeAlias = Literal[
    "PUBLISH",
    "SUBSCRIBE",
    "RECEIVE",
    "CONNECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISH",
        "SUBSCRIBE",
        "RECEIVE",
        "CONNECT",
    )
)


def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)
