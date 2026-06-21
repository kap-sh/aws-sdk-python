"""Generated from Smithy shape ``com.amazonaws.connect#IvrRecordingTrack``."""

from typing import Literal, TypeAlias, cast

IvrRecordingTrack: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: IvrRecordingTrack) -> str:
    return value


def deserialize_json(data: str) -> IvrRecordingTrack:
    return cast(IvrRecordingTrack, data)
