"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal["Mbps_Outbound_Bandwidth",]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
