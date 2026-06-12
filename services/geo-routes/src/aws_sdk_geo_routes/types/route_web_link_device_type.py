"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWebLinkDeviceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteWebLinkDeviceType: TypeAlias = Literal[
    "Android",
    "Ios",
    "Web",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Android",
        "Ios",
        "Web",
    )
)


def serialize_json(value: RouteWebLinkDeviceType) -> str:
    return value


def deserialize_json(data: str) -> RouteWebLinkDeviceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteWebLinkDeviceType value: {data!r}")
    return cast(RouteWebLinkDeviceType, data)
