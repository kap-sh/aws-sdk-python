"""Generated from Smithy shape ``com.amazonaws.connect#Recordings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.recording_info

Recordings: TypeAlias = list["aws_sdk_connect.types.recording_info.RecordingInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: Recordings) -> list:
    import aws_sdk_connect.types.recording_info

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.recording_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> Recordings:
    import aws_sdk_connect.types.recording_info

    out: Recordings = []
    for item in data:
        out.append(aws_sdk_connect.types.recording_info.deserialize_json(item))
    return out
