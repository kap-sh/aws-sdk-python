"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafIntervalCadence``."""

from typing import Literal, TypeAlias, cast

"""The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval. If set to FOLLOW_SEGMENTATION, MediaConvert generates thumbnail playlist entries that align exactly with video segment boundaries. FOLLOW_SEGMENTATION requires 1x1 tiling."""
CmafIntervalCadence: TypeAlias = Literal[
    "FOLLOW_IFRAME",
    "FOLLOW_CUSTOM",
    "FOLLOW_SEGMENTATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafIntervalCadence) -> str:
    return value


def deserialize_json(data: str) -> CmafIntervalCadence:
    return cast(CmafIntervalCadence, data)
