"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoMpdManifestBandwidthType``."""

from typing import Literal, TypeAlias, cast

"""Specify how the value for bandwidth is determined for each video Representation in your output MPD manifest. We recommend that you choose a MPD manifest bandwidth type that is compatible with your downstream player configuration. Max: Use the same value that you specify for Max bitrate in the video output, in bits per second. Average: Use the calculated average bitrate of the encoded video output, in bits per second."""
DashIsoMpdManifestBandwidthType: TypeAlias = Literal[
    "AVERAGE",
    "MAX",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashIsoMpdManifestBandwidthType) -> str:
    return value


def deserialize_json(data: str) -> DashIsoMpdManifestBandwidthType:
    return cast(DashIsoMpdManifestBandwidthType, data)
