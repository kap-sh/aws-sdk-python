"""Generated from Smithy shape ``com.amazonaws.mediatailor#AlertCategory``."""

from typing import Literal, TypeAlias, cast

AlertCategory: TypeAlias = Literal[
    "SCHEDULING_ERROR",
    "PLAYBACK_WARNING",
    "INFO",
]


# --- restJson1 ser/de ---
def serialize_json(value: AlertCategory) -> str:
    return value


def deserialize_json(data: str) -> AlertCategory:
    return cast(AlertCategory, data)
