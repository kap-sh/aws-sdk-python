"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.hls_settings


class OutputSettings(TypedDict):
    hls_settings: NotRequired["aws_sdk_mediaconvert.types.hls_settings.HlsSettings"]
    """Settings for HLS output groups"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputSettings) -> dict:
    out: dict = {}
    if "hls_settings" in value:
        import aws_sdk_mediaconvert.types.hls_settings

        out["hlsSettings"] = aws_sdk_mediaconvert.types.hls_settings.serialize_json(
            value["hls_settings"]
        )
    return out


def deserialize_json(data: dict) -> OutputSettings:
    out: OutputSettings = {}  # type: ignore[typeddict-item]
    if "hlsSettings" in data:
        import aws_sdk_mediaconvert.types.hls_settings

        out["hls_settings"] = aws_sdk_mediaconvert.types.hls_settings.deserialize_json(
            data["hlsSettings"]
        )
    return out
