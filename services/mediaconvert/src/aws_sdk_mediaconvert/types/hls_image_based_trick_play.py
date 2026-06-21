"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsImageBasedTrickPlay``."""

from typing import Literal, TypeAlias, cast

"""Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. Choose Advanced to customize thumbnail and tile settings for a single trick play variant. Choose Variants to specify multiple trick play variants, each with its own thumbnail and tile settings. MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md"""
HlsImageBasedTrickPlay: TypeAlias = Literal[
    "NONE",
    "THUMBNAIL",
    "THUMBNAIL_AND_FULLFRAME",
    "ADVANCED",
    "VARIANTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsImageBasedTrickPlay) -> str:
    return value


def deserialize_json(data: str) -> HlsImageBasedTrickPlay:
    return cast(HlsImageBasedTrickPlay, data)
