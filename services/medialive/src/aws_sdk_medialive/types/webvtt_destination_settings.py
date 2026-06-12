"""Generated from Smithy shape ``com.amazonaws.medialive#WebvttDestinationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.webvtt_destination_style_control


class WebvttDestinationSettings(TypedDict):
    style_control: NotRequired[
        "aws_sdk_medialive.types.webvtt_destination_style_control.WebvttDestinationStyleControl"
    ]
    """Controls whether the color and position of the source captions is passed through to the WebVTT output captions. PASSTHROUGH - Valid only if the source captions are EMBEDDED or TELETEXT. NO_STYLE_DATA - Don't pass through the style. The output captions will not contain any font styling information."""


# --- restJson1 ser/de ---
def serialize_json(value: WebvttDestinationSettings) -> dict:
    out: dict = {}
    if "style_control" in value:
        import aws_sdk_medialive.types.webvtt_destination_style_control

        out["styleControl"] = (
            aws_sdk_medialive.types.webvtt_destination_style_control.serialize_json(
                value["style_control"]
            )
        )
    return out


def deserialize_json(data: dict) -> WebvttDestinationSettings:
    out: WebvttDestinationSettings = {}  # type: ignore[typeddict-item]
    if "styleControl" in data:
        import aws_sdk_medialive.types.webvtt_destination_style_control

        out["style_control"] = (
            aws_sdk_medialive.types.webvtt_destination_style_control.deserialize_json(
                data["styleControl"]
            )
        )
    return out
