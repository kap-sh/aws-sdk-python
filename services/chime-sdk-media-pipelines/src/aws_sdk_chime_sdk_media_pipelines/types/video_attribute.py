"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VideoAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.border_color
    import aws_sdk_chime_sdk_media_pipelines.types.border_thickness
    import aws_sdk_chime_sdk_media_pipelines.types.corner_radius
    import aws_sdk_chime_sdk_media_pipelines.types.highlight_color


class VideoAttribute(TypedDict):
    corner_radius: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.corner_radius.CornerRadius"
    ]
    """<p>Sets the corner radius of all video tiles.</p>"""
    border_color: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.border_color.BorderColor"
    ]
    """<p>Defines the border color of all video tiles.</p>"""
    highlight_color: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.highlight_color.HighlightColor"
    ]
    """<p>Defines the highlight color for the active video tile.</p>"""
    border_thickness: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.border_thickness.BorderThickness"
    ]
    """<p>Defines the border thickness for all video tiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoAttribute) -> dict:
    out: dict = {}
    if "corner_radius" in value:
        out["CornerRadius"] = value["corner_radius"]
    if "border_color" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.border_color

        out["BorderColor"] = (
            aws_sdk_chime_sdk_media_pipelines.types.border_color.serialize_json(
                value["border_color"]
            )
        )
    if "highlight_color" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.highlight_color

        out["HighlightColor"] = (
            aws_sdk_chime_sdk_media_pipelines.types.highlight_color.serialize_json(
                value["highlight_color"]
            )
        )
    if "border_thickness" in value:
        out["BorderThickness"] = value["border_thickness"]
    return out


def deserialize_json(data: dict) -> VideoAttribute:
    out: VideoAttribute = {}  # type: ignore[typeddict-item]
    if "CornerRadius" in data:
        out["corner_radius"] = data["CornerRadius"]
    if "BorderColor" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.border_color

        out["border_color"] = (
            aws_sdk_chime_sdk_media_pipelines.types.border_color.deserialize_json(
                data["BorderColor"]
            )
        )
    if "HighlightColor" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.highlight_color

        out["highlight_color"] = (
            aws_sdk_chime_sdk_media_pipelines.types.highlight_color.deserialize_json(
                data["HighlightColor"]
            )
        )
    if "BorderThickness" in data:
        out["border_thickness"] = data["BorderThickness"]
    return out
