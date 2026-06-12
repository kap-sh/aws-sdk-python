"""Generated from Smithy shape ``com.amazonaws.connect#LexVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

LexVersion: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1",
        "V2",
    )
)


def serialize_json(value: LexVersion) -> str:
    return value


def deserialize_json(data: str) -> LexVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LexVersion value: {data!r}")
    return cast(LexVersion, data)
