"""Generated from Smithy shape ``com.amazonaws.medialive#AribSourceSettings``."""

from typing_extensions import TypedDict


class AribSourceSettings(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AribSourceSettings) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AribSourceSettings:
    out: AribSourceSettings = {}  # type: ignore[typeddict-item]
    return out
