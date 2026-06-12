"""Generated from Smithy shape ``com.amazonaws.connect#OperationalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

OperationalStatus: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "CLOSED",
    )
)


def serialize_json(value: OperationalStatus) -> str:
    return value


def deserialize_json(data: str) -> OperationalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationalStatus value: {data!r}")
    return cast(OperationalStatus, data)
