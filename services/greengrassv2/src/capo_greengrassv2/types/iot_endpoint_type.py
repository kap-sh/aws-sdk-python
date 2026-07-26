"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IotEndpointType``."""

from typing import Literal, TypeAlias, cast

IotEndpointType: TypeAlias = Literal[
    "fips",
    "standard",
]


# --- restJson1 ser/de ---
def serialize_json(value: IotEndpointType) -> str:
    return value


def deserialize_json(data: str) -> IotEndpointType:
    return cast(IotEndpointType, data)
