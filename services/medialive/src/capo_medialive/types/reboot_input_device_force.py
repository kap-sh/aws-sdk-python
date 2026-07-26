"""Generated from Smithy shape ``com.amazonaws.medialive#RebootInputDeviceForce``."""

from typing import Literal, TypeAlias, cast

"""Whether or not to force reboot the input device."""
RebootInputDeviceForce: TypeAlias = Literal[
    "NO",
    "YES",
]


# --- restJson1 ser/de ---
def serialize_json(value: RebootInputDeviceForce) -> str:
    return value


def deserialize_json(data: str) -> RebootInputDeviceForce:
    return cast(RebootInputDeviceForce, data)
