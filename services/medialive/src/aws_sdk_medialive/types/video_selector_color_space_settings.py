"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelectorColorSpaceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.hdr10_settings


class VideoSelectorColorSpaceSettings(TypedDict):
    hdr10_settings: NotRequired["aws_sdk_medialive.types.hdr10_settings.Hdr10Settings"]


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelectorColorSpaceSettings) -> dict:
    out: dict = {}
    if "hdr10_settings" in value:
        import aws_sdk_medialive.types.hdr10_settings

        out["hdr10Settings"] = aws_sdk_medialive.types.hdr10_settings.serialize_json(
            value["hdr10_settings"]
        )
    return out


def deserialize_json(data: dict) -> VideoSelectorColorSpaceSettings:
    out: VideoSelectorColorSpaceSettings = {}  # type: ignore[typeddict-item]
    if "hdr10Settings" in data:
        import aws_sdk_medialive.types.hdr10_settings

        out["hdr10_settings"] = aws_sdk_medialive.types.hdr10_settings.deserialize_json(
            data["hdr10Settings"]
        )
    return out
