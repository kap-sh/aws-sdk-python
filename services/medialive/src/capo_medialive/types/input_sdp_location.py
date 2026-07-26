"""Generated from Smithy shape ``com.amazonaws.medialive#InputSdpLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer
    import capo_medialive.types.__string


class InputSdpLocation(TypedDict, closed=True):
    media_index: NotRequired["capo_medialive.types.__integer.__integer"]
    """The index of the media stream in the SDP file for one SMPTE 2110 stream."""
    sdp_url: NotRequired["capo_medialive.types.__string.__string"]
    """The URL of the SDP file for one SMPTE 2110 stream."""


# --- restJson1 ser/de ---
def serialize_json(value: InputSdpLocation) -> dict:
    out: dict = {}
    if "media_index" in value:
        out["mediaIndex"] = value["media_index"]
    if "sdp_url" in value:
        out["sdpUrl"] = value["sdp_url"]
    return out


def deserialize_json(data: dict) -> InputSdpLocation:
    out: InputSdpLocation = {}  # type: ignore[typeddict-item]
    if "mediaIndex" in data:
        out["media_index"] = data["mediaIndex"]
    if "sdpUrl" in data:
        out["sdp_url"] = data["sdpUrl"]
    return out
