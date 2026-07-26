"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#MediaPlacementNetworkType``."""

from typing import Literal, TypeAlias, cast

MediaPlacementNetworkType: TypeAlias = Literal[
    "Ipv4Only",
    "DualStack",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPlacementNetworkType) -> str:
    return value


def deserialize_json(data: str) -> MediaPlacementNetworkType:
    return cast(MediaPlacementNetworkType, data)
