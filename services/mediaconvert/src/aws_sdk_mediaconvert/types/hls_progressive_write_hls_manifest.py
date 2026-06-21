"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsProgressiveWriteHlsManifest``."""

from typing import Literal, TypeAlias, cast

"""Specify whether MediaConvert generates HLS manifests while your job is running or when your job is complete. To generate HLS manifests while your job is running: Choose Enabled. Use if you want to play back your content as soon as it's available. MediaConvert writes the parent and child manifests after the first three media segments are written to your destination S3 bucket. It then writes new updated manifests after each additional segment is written. The parent manifest includes the latest BANDWIDTH and AVERAGE-BANDWIDTH attributes, and child manifests include the latest available media segment. When your job completes, the final child playlists include an EXT-X-ENDLIST tag. To generate HLS manifests only when your job completes: Choose Disabled."""
HlsProgressiveWriteHlsManifest: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsProgressiveWriteHlsManifest) -> str:
    return value


def deserialize_json(data: str) -> HlsProgressiveWriteHlsManifest:
    return cast(HlsProgressiveWriteHlsManifest, data)
