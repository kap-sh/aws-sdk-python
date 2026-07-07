"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeBurninSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string_max255
    import aws_sdk_medialive.types.timecode_burnin_font_size
    import aws_sdk_medialive.types.timecode_burnin_position


class TimecodeBurninSettings(TypedDict, closed=True):
    font_size: NotRequired[
        "aws_sdk_medialive.types.timecode_burnin_font_size.TimecodeBurninFontSize"
    ]
    """Choose a timecode burn-in font size"""
    position: NotRequired[
        "aws_sdk_medialive.types.timecode_burnin_position.TimecodeBurninPosition"
    ]
    """Choose a timecode burn-in output position"""
    prefix: NotRequired["aws_sdk_medialive.types.__string_max255.__stringMax255"]
    """Create a timecode burn-in prefix (optional)"""


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeBurninSettings) -> dict:
    out: dict = {}
    if "font_size" in value:
        import aws_sdk_medialive.types.timecode_burnin_font_size

        out["fontSize"] = (
            aws_sdk_medialive.types.timecode_burnin_font_size.serialize_json(
                value["font_size"]
            )
        )
    if "position" in value:
        import aws_sdk_medialive.types.timecode_burnin_position

        out["position"] = (
            aws_sdk_medialive.types.timecode_burnin_position.serialize_json(
                value["position"]
            )
        )
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> TimecodeBurninSettings:
    out: TimecodeBurninSettings = {}  # type: ignore[typeddict-item]
    if "fontSize" in data:
        import aws_sdk_medialive.types.timecode_burnin_font_size

        out["font_size"] = (
            aws_sdk_medialive.types.timecode_burnin_font_size.deserialize_json(
                data["fontSize"]
            )
        )
    if "position" in data:
        import aws_sdk_medialive.types.timecode_burnin_position

        out["position"] = (
            aws_sdk_medialive.types.timecode_burnin_position.deserialize_json(
                data["position"]
            )
        )
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
