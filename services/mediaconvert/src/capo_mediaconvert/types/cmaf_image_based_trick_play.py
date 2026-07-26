"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafImageBasedTrickPlay``."""

from typing import Literal, TypeAlias, cast

"""Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. Choose Advanced to customize thumbnail and tile settings for a single trick play variant. Choose Variants to specify multiple trick play variants, each with its own thumbnail and tile settings. When you enable Write HLS manifest, MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. When you enable Write DASH manifest, MediaConvert adds an entry in the .mpd manifest for each set of images that you generate. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md"""
CmafImageBasedTrickPlay: TypeAlias = Literal[
    "NONE",
    "THUMBNAIL",
    "THUMBNAIL_AND_FULLFRAME",
    "ADVANCED",
    "VARIANTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafImageBasedTrickPlay) -> str:
    return value


def deserialize_json(data: str) -> CmafImageBasedTrickPlay:
    return cast(CmafImageBasedTrickPlay, data)
