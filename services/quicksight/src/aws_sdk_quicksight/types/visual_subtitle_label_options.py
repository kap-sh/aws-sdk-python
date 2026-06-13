"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualSubtitleLabelOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.long_format_text
    import aws_sdk_quicksight.types.visibility


class VisualSubtitleLabelOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the subtitle label.</p>"""
    format_text: NotRequired["aws_sdk_quicksight.types.long_format_text.LongFormatText"]
    """<p>The long text format of the subtitle label, such as plain text or rich text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualSubtitleLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "format_text" in value:
        import aws_sdk_quicksight.types.long_format_text

        out["FormatText"] = aws_sdk_quicksight.types.long_format_text.serialize_json(
            value["format_text"]
        )
    return out


def deserialize_json(data: dict) -> VisualSubtitleLabelOptions:
    out: VisualSubtitleLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "FormatText" in data:
        import aws_sdk_quicksight.types.long_format_text

        out["format_text"] = aws_sdk_quicksight.types.long_format_text.deserialize_json(
            data["FormatText"]
        )
    return out
