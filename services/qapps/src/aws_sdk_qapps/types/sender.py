"""Generated from Smithy shape ``com.amazonaws.qapps#Sender``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

Sender: TypeAlias = Literal[
    "USER",
    "SYSTEM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "SYSTEM",
    )
)


def serialize_json(value: Sender) -> str:
    return value


def deserialize_json(data: str) -> Sender:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Sender value: {data!r}")
    return cast(Sender, data)
