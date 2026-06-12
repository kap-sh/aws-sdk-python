"""Generated from Smithy shape ``com.amazonaws.connect#AllowedUserAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AllowedUserAction: TypeAlias = Literal[
    "CALL",
    "DISCARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CALL",
        "DISCARD",
    )
)


def serialize_json(value: AllowedUserAction) -> str:
    return value


def deserialize_json(data: str) -> AllowedUserAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowedUserAction value: {data!r}")
    return cast(AllowedUserAction, data)
