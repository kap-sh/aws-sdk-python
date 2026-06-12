"""Generated from Smithy shape ``com.amazonaws.cognitosync#Operation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_sync.errors import DeserializationError

Operation: TypeAlias = Literal[
    "replace",
    "remove",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "replace",
        "remove",
    )
)


def serialize_json(value: Operation) -> str:
    return value


def deserialize_json(data: str) -> Operation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operation value: {data!r}")
    return cast(Operation, data)
