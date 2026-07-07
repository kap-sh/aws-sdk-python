"""Generated from Smithy shape ``com.amazonaws.medialive#MotionGraphicsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.html_motion_graphics_settings


class MotionGraphicsSettings(TypedDict, closed=True):
    html_motion_graphics_settings: NotRequired[
        "aws_sdk_medialive.types.html_motion_graphics_settings.HtmlMotionGraphicsSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MotionGraphicsSettings) -> dict:
    out: dict = {}
    if "html_motion_graphics_settings" in value:
        import aws_sdk_medialive.types.html_motion_graphics_settings

        out["htmlMotionGraphicsSettings"] = (
            aws_sdk_medialive.types.html_motion_graphics_settings.serialize_json(
                value["html_motion_graphics_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MotionGraphicsSettings:
    out: MotionGraphicsSettings = {}  # type: ignore[typeddict-item]
    if "htmlMotionGraphicsSettings" in data:
        import aws_sdk_medialive.types.html_motion_graphics_settings

        out["html_motion_graphics_settings"] = (
            aws_sdk_medialive.types.html_motion_graphics_settings.deserialize_json(
                data["htmlMotionGraphicsSettings"]
            )
        )
    return out
