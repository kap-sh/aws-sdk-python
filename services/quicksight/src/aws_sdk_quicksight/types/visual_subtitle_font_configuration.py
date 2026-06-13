"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualSubtitleFontConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.horizontal_text_alignment
    import aws_sdk_quicksight.types.text_transform


class VisualSubtitleFontConfiguration(TypedDict):
    font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    text_alignment: NotRequired[
        "aws_sdk_quicksight.types.horizontal_text_alignment.HorizontalTextAlignment"
    ]
    """<p>Determines the alignment of visual sub-title.</p>"""
    text_transform: NotRequired["aws_sdk_quicksight.types.text_transform.TextTransform"]
    """<p>Determines the text transformation of visual sub-title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualSubtitleFontConfiguration) -> dict:
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
    if "text_transform" in value:
        import aws_sdk_quicksight.types.text_transform

        out["TextTransform"] = aws_sdk_quicksight.types.text_transform.serialize_json(
            value["text_transform"]
        )
    return out


def deserialize_json(data: dict) -> VisualSubtitleFontConfiguration:
    out: VisualSubtitleFontConfiguration = {}  # type: ignore[typeddict-item]
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
    if "TextTransform" in data:
        import aws_sdk_quicksight.types.text_transform

        out["text_transform"] = (
            aws_sdk_quicksight.types.text_transform.deserialize_json(
                data["TextTransform"]
            )
        )
    return out
