"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ResourceContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

ResourceContentType: TypeAlias = Literal[
    "EMAIL",
    "PHONE_NUMBER",
    "LINK",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL",
        "PHONE_NUMBER",
        "LINK",
        "OTHER",
    )
)


def serialize_json(value: ResourceContentType) -> str:
    return value


def deserialize_json(data: str) -> ResourceContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceContentType value: {data!r}")
    return cast(ResourceContentType, data)
