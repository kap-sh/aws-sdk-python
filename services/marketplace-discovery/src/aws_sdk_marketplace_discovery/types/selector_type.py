"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

SelectorType: TypeAlias = Literal["Duration",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Duration",))


def serialize_json(value: SelectorType) -> str:
    return value


def deserialize_json(data: str) -> SelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectorType value: {data!r}")
    return cast(SelectorType, data)
