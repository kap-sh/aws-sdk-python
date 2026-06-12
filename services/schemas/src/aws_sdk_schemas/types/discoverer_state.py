"""Generated from Smithy shape ``com.amazonaws.schemas#DiscovererState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_schemas.errors import DeserializationError

DiscovererState: TypeAlias = Literal[
    "STARTED",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTED",
        "STOPPED",
    )
)


def serialize_json(value: DiscovererState) -> str:
    return value


def deserialize_json(data: str) -> DiscovererState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiscovererState value: {data!r}")
    return cast(DiscovererState, data)
