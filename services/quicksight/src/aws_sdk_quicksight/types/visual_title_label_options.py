"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualTitleLabelOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_format_text
    import aws_sdk_quicksight.types.visibility


class VisualTitleLabelOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the title label.</p>"""
    format_text: NotRequired[
        "aws_sdk_quicksight.types.short_format_text.ShortFormatText"
    ]
    """<p>The short text format of the title label, such as plain text or rich text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualTitleLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "format_text" in value:
        import aws_sdk_quicksight.types.short_format_text

        out["FormatText"] = aws_sdk_quicksight.types.short_format_text.serialize_json(
            value["format_text"]
        )
    return out


def deserialize_json(data: dict) -> VisualTitleLabelOptions:
    out: VisualTitleLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "FormatText" in data:
        import aws_sdk_quicksight.types.short_format_text

        out["format_text"] = (
            aws_sdk_quicksight.types.short_format_text.deserialize_json(
                data["FormatText"]
            )
        )
    return out
