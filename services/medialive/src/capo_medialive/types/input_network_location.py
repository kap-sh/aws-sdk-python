"""Generated from Smithy shape ``com.amazonaws.medialive#InputNetworkLocation``."""

from typing import Literal, TypeAlias, cast

"""With the introduction of MediaLive Anywhere, a MediaLive input can now exist in two different places: AWS or inside an on-premises datacenter. By default all inputs will continue to be AWS inputs."""
InputNetworkLocation: TypeAlias = Literal[
    "AWS",
    "ON_PREMISES",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputNetworkLocation) -> str:
    return value


def deserialize_json(data: str) -> InputNetworkLocation:
    return cast(InputNetworkLocation, data)
