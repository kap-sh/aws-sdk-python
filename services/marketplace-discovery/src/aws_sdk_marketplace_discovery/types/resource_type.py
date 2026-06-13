"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "MANUFACTURER_SUPPORT",
    "MANUFACTURER_INSTRUCTIONS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANUFACTURER_SUPPORT",
        "MANUFACTURER_INSTRUCTIONS",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
