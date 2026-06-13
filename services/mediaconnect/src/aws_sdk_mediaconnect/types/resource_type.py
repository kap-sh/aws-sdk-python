"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

ResourceType: TypeAlias = Literal["Mbps_Outbound_Bandwidth",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Mbps_Outbound_Bandwidth",))


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
