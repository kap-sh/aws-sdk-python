"""Generated from Smithy shape ``com.amazonaws.ram#ResourceRegionScopeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceRegionScopeFilter: TypeAlias = Literal[
    "ALL",
    "REGIONAL",
    "GLOBAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "REGIONAL",
        "GLOBAL",
    )
)


def serialize_json(value: ResourceRegionScopeFilter) -> str:
    return value


def deserialize_json(data: str) -> ResourceRegionScopeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceRegionScopeFilter value: {data!r}")
    return cast(ResourceRegionScopeFilter, data)
