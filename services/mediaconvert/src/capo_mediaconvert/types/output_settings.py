"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.hls_settings


class OutputSettings(TypedDict, closed=True):
    hls_settings: NotRequired["capo_mediaconvert.types.hls_settings.HlsSettings"]
    """Settings for HLS output groups"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputSettings) -> dict:
    out: dict = {}
    if "hls_settings" in value:
        import capo_mediaconvert.types.hls_settings

        out["hlsSettings"] = capo_mediaconvert.types.hls_settings.serialize_json(
            value["hls_settings"]
        )
    return out


def deserialize_json(data: dict) -> OutputSettings:
    out: OutputSettings = {}  # type: ignore[typeddict-item]
    if "hlsSettings" in data:
        import capo_mediaconvert.types.hls_settings

        out["hls_settings"] = capo_mediaconvert.types.hls_settings.deserialize_json(
            data["hlsSettings"]
        )
    return out
