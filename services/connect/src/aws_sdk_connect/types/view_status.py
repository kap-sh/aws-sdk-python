"""Generated from Smithy shape ``com.amazonaws.connect#ViewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ViewStatus: TypeAlias = Literal[
    "PUBLISHED",
    "SAVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISHED",
        "SAVED",
    )
)


def serialize_json(value: ViewStatus) -> str:
    return value


def deserialize_json(data: str) -> ViewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ViewStatus value: {data!r}")
    return cast(ViewStatus, data)
