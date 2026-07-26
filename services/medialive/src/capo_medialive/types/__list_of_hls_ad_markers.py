"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfHlsAdMarkers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.hls_ad_markers

__listOfHlsAdMarkers: TypeAlias = list[
    "capo_medialive.types.hls_ad_markers.HlsAdMarkers"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsAdMarkers) -> list:
    import capo_medialive.types.hls_ad_markers

    out: list = []
    for item in value:
        out.append(capo_medialive.types.hls_ad_markers.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfHlsAdMarkers:
    import capo_medialive.types.hls_ad_markers

    out: __listOfHlsAdMarkers = []
    for item in data:
        out.append(capo_medialive.types.hls_ad_markers.deserialize_json(item))
    return out
