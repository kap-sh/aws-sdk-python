"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceIpScheme``."""

from typing import Literal, TypeAlias, cast

"""Specifies whether the input device has been configured (outside of MediaLive) to use a dynamic IP address assignment (DHCP) or a static IP address."""
InputDeviceIpScheme: TypeAlias = Literal[
    "STATIC",
    "DHCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceIpScheme) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceIpScheme:
    return cast(InputDeviceIpScheme, data)
