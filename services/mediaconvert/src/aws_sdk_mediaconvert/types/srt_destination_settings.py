"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SrtDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.srt_style_passthrough


class SrtDestinationSettings(TypedDict, closed=True):
    style_passthrough: NotRequired[
        "aws_sdk_mediaconvert.types.srt_style_passthrough.SrtStylePassthrough"
    ]
    """Set Style passthrough to ENABLED to use the available style, color, and position information from your input captions. MediaConvert uses default settings for any missing style and position information in your input captions. Set Style passthrough to DISABLED, or leave blank, to ignore the style and position information from your input captions and use simplified output captions."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtDestinationSettings) -> dict:
    out: dict = {}
    if "style_passthrough" in value:
        import aws_sdk_mediaconvert.types.srt_style_passthrough

        out["stylePassthrough"] = (
            aws_sdk_mediaconvert.types.srt_style_passthrough.serialize_json(
                value["style_passthrough"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtDestinationSettings:
    out: SrtDestinationSettings = {}  # type: ignore[typeddict-item]
    if "stylePassthrough" in data:
        import aws_sdk_mediaconvert.types.srt_style_passthrough

        out["style_passthrough"] = (
            aws_sdk_mediaconvert.types.srt_style_passthrough.deserialize_json(
                data["stylePassthrough"]
            )
        )
    return out
