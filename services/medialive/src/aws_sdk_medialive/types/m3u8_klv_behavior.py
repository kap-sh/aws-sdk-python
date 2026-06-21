"""Generated from Smithy shape ``com.amazonaws.medialive#M3u8KlvBehavior``."""

from typing import Literal, TypeAlias, cast

"""M3u8 Klv Behavior"""
M3u8KlvBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M3u8KlvBehavior) -> str:
    return value


def deserialize_json(data: str) -> M3u8KlvBehavior:
    return cast(M3u8KlvBehavior, data)
