"""Generated from Smithy shape ``com.amazonaws.iot#NamedShadowIndexingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

NamedShadowIndexingMode: TypeAlias = Literal[
    "OFF",
    "ON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "ON",
    )
)


def serialize_json(value: NamedShadowIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> NamedShadowIndexingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamedShadowIndexingMode value: {data!r}")
    return cast(NamedShadowIndexingMode, data)
