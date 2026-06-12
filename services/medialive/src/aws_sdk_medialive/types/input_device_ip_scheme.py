"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceIpScheme``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Specifies whether the input device has been configured (outside of MediaLive) to use a dynamic IP address assignment (DHCP) or a static IP address."""
InputDeviceIpScheme: TypeAlias = Literal[
    "STATIC",
    "DHCP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATIC",
        "DHCP",
    )
)


def serialize_json(value: InputDeviceIpScheme) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceIpScheme:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeviceIpScheme value: {data!r}")
    return cast(InputDeviceIpScheme, data)
