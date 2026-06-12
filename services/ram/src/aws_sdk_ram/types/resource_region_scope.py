"""Generated from Smithy shape ``com.amazonaws.ram#ResourceRegionScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceRegionScope: TypeAlias = Literal[
    "REGIONAL",
    "GLOBAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGIONAL",
        "GLOBAL",
    )
)


def serialize_json(value: ResourceRegionScope) -> str:
    return value


def deserialize_json(data: str) -> ResourceRegionScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceRegionScope value: {data!r}")
    return cast(ResourceRegionScope, data)
