"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoSelectorMode``."""

from typing import Literal, TypeAlias, cast

"""AUTO will select the highest bitrate input in the video selector source. REMUX_ALL will passthrough all the selected streams in the video selector source. When selecting streams from multiple renditions (i.e. using Stream video selector type): REMUX_ALL will only remux all streams selected, and AUTO will use the highest bitrate video stream among the selected streams as source."""
VideoSelectorMode: TypeAlias = Literal[
    "AUTO",
    "REMUX_ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelectorMode) -> str:
    return value


def deserialize_json(data: str) -> VideoSelectorMode:
    return cast(VideoSelectorMode, data)
