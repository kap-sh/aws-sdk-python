"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

QuickConnectType: TypeAlias = Literal[
    "USER",
    "QUEUE",
    "PHONE_NUMBER",
    "FLOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "QUEUE",
        "PHONE_NUMBER",
        "FLOW",
    )
)


def serialize_json(value: QuickConnectType) -> str:
    return value


def deserialize_json(data: str) -> QuickConnectType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuickConnectType value: {data!r}")
    return cast(QuickConnectType, data)
