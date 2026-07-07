"""Generated from Smithy shape ``com.amazonaws.quicksight#ControlTitleFontConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.horizontal_text_alignment


class ControlTitleFontConfiguration(TypedDict, closed=True):
    font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>Configures the font settings for the control title.</p>"""
    text_alignment: NotRequired[
        "aws_sdk_quicksight.types.horizontal_text_alignment.HorizontalTextAlignment"
    ]
    """<p>Determines the alignment of the control title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlTitleFontConfiguration) -> dict:
    out: dict = {}
    if "font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["FontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["font_configuration"]
            )
        )
    if "text_alignment" in value:
        import aws_sdk_quicksight.types.horizontal_text_alignment

        out["TextAlignment"] = (
            aws_sdk_quicksight.types.horizontal_text_alignment.serialize_json(
                value["text_alignment"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlTitleFontConfiguration:
    out: ControlTitleFontConfiguration = {}  # type: ignore[typeddict-item]
    if "FontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["FontConfiguration"]
            )
        )
    if "TextAlignment" in data:
        import aws_sdk_quicksight.types.horizontal_text_alignment

        out["text_alignment"] = (
            aws_sdk_quicksight.types.horizontal_text_alignment.deserialize_json(
                data["TextAlignment"]
            )
        )
    return out
