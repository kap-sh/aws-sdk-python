"""Generated from Smithy shape ``com.amazonaws.arczonalshift#BlockedWindows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.blocked_window

BlockedWindows: TypeAlias = list[
    "aws_sdk_arc_zonal_shift.types.blocked_window.BlockedWindow"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlockedWindows) -> list:
    return list(value)


def deserialize_json(data: list) -> BlockedWindows:
    return list(data)
