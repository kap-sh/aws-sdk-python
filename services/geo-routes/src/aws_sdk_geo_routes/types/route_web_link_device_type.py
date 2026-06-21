"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWebLinkDeviceType``."""

from typing import Literal, TypeAlias, cast

RouteWebLinkDeviceType: TypeAlias = Literal[
    "Android",
    "Ios",
    "Web",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteWebLinkDeviceType) -> str:
    return value


def deserialize_json(data: str) -> RouteWebLinkDeviceType:
    return cast(RouteWebLinkDeviceType, data)
