"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AllowedWindows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.allowed_window

AllowedWindows: TypeAlias = list[
    "aws_sdk_arc_zonal_shift.types.allowed_window.AllowedWindow"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedWindows) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedWindows:
    return list(data)
