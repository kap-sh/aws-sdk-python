"""Generated from Smithy shape ``com.amazonaws.connect#Recordings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.recording_info

Recordings: TypeAlias = list["capo_connect.types.recording_info.RecordingInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: Recordings) -> list:
    import capo_connect.types.recording_info

    out: list = []
    for item in value:
        out.append(capo_connect.types.recording_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> Recordings:
    import capo_connect.types.recording_info

    out: Recordings = []
    for item in data:
        out.append(capo_connect.types.recording_info.deserialize_json(item))
    return out
