"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ConnectionScope: TypeAlias = Literal[
    "DOMAIN",
    "PROJECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOMAIN",
        "PROJECT",
    )
)


def serialize_json(value: ConnectionScope) -> str:
    return value


def deserialize_json(data: str) -> ConnectionScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionScope value: {data!r}")
    return cast(ConnectionScope, data)
