"""Generated from Smithy shape ``com.amazonaws.mediatailor#Mode``."""

from typing import Literal, TypeAlias, cast

Mode: TypeAlias = Literal[
    "OFF",
    "BEHIND_LIVE_EDGE",
    "AFTER_LIVE_EDGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mode) -> str:
    return value


def deserialize_json(data: str) -> Mode:
    return cast(Mode, data)
