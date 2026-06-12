"""Generated from Smithy shape ``com.amazonaws.medialive#RebootInputDeviceForce``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Whether or not to force reboot the input device."""
RebootInputDeviceForce: TypeAlias = Literal[
    "NO",
    "YES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO",
        "YES",
    )
)


def serialize_json(value: RebootInputDeviceForce) -> str:
    return value


def deserialize_json(data: str) -> RebootInputDeviceForce:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RebootInputDeviceForce value: {data!r}")
    return cast(RebootInputDeviceForce, data)
