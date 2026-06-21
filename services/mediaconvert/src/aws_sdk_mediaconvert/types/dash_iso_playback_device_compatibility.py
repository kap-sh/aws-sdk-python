"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoPlaybackDeviceCompatibility``."""

from typing import Literal, TypeAlias, cast

"""This setting can improve the compatibility of your output with video players on obsolete devices. It applies only to DASH H.264 outputs with DRM encryption. Choose Unencrypted SEI only to correct problems with playback on older devices. Otherwise, keep the default setting CENC v1. If you choose Unencrypted SEI, for that output, the service will exclude the access unit delimiter and will leave the SEI NAL units unencrypted."""
DashIsoPlaybackDeviceCompatibility: TypeAlias = Literal[
    "CENC_V1",
    "UNENCRYPTED_SEI",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashIsoPlaybackDeviceCompatibility) -> str:
    return value


def deserialize_json(data: str) -> DashIsoPlaybackDeviceCompatibility:
    return cast(DashIsoPlaybackDeviceCompatibility, data)
