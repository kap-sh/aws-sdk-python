"""Generated from Smithy shape ``com.amazonaws.qapps#Action``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

Action: TypeAlias = Literal[
    "read",
    "write",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "read",
        "write",
    )
)


def serialize_json(value: Action) -> str:
    return value


def deserialize_json(data: str) -> Action:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Action value: {data!r}")
    return cast(Action, data)
