"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controlcatalog.errors import DeserializationError

ControlScope: TypeAlias = Literal[
    "GLOBAL",
    "REGIONAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GLOBAL",
        "REGIONAL",
    )
)


def serialize_json(value: ControlScope) -> str:
    return value


def deserialize_json(data: str) -> ControlScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlScope value: {data!r}")
    return cast(ControlScope, data)
