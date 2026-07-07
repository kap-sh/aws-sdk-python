"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualTitleFontConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.horizontal_text_alignment
    import aws_sdk_quicksight.types.text_transform


class VisualTitleFontConfiguration(TypedDict, closed=True):
    font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    text_alignment: NotRequired[
        "aws_sdk_quicksight.types.horizontal_text_alignment.HorizontalTextAlignment"
    ]
    """<p>Determines the alignment of visual title.</p>"""
    text_transform: NotRequired["aws_sdk_quicksight.types.text_transform.TextTransform"]
    """<p>Determines the text transformation of visual title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualTitleFontConfiguration) -> dict:
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


def deserialize_json(data: dict) -> VisualTitleFontConfiguration:
    out: VisualTitleFontConfiguration = {}  # type: ignore[typeddict-item]
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
