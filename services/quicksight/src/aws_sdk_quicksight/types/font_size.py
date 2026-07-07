"""Generated from Smithy shape ``com.amazonaws.quicksight#FontSize``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pixel_length
    import aws_sdk_quicksight.types.relative_font_size


class FontSize(TypedDict, closed=True):
    relative: NotRequired[
        "aws_sdk_quicksight.types.relative_font_size.RelativeFontSize"
    ]
    """<p>The lexical name for the text size, proportional to its surrounding context.</p>"""
    absolute: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>The font size that you want to use in px.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FontSize) -> dict:
    out: dict = {}
    if "relative" in value:
        import aws_sdk_quicksight.types.relative_font_size

        out["Relative"] = aws_sdk_quicksight.types.relative_font_size.serialize_json(
            value["relative"]
        )
    if "absolute" in value:
        out["Absolute"] = value["absolute"]
    return out


def deserialize_json(data: dict) -> FontSize:
    out: FontSize = {}  # type: ignore[typeddict-item]
    if "Relative" in data:
        import aws_sdk_quicksight.types.relative_font_size

        out["relative"] = aws_sdk_quicksight.types.relative_font_size.deserialize_json(
            data["Relative"]
        )
    if "Absolute" in data:
        out["absolute"] = data["Absolute"]
    return out
