"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MpdCaptionContainerType``."""

from typing import Literal, TypeAlias, cast

"""Use this setting only in DASH output groups that include sidecar TTML, IMSC or WEBVTT captions. You specify sidecar captions in a separate output from your audio and video. Choose Raw for captions in a single XML file in a raw container. Choose Fragmented MPEG-4 for captions in XML format contained within fragmented MP4 files. This set of fragmented MP4 files is separate from your video and audio fragmented MP4 files."""
MpdCaptionContainerType: TypeAlias = Literal[
    "RAW",
    "FRAGMENTED_MP4",
]


# --- restJson1 ser/de ---
def serialize_json(value: MpdCaptionContainerType) -> str:
    return value


def deserialize_json(data: str) -> MpdCaptionContainerType:
    return cast(MpdCaptionContainerType, data)
