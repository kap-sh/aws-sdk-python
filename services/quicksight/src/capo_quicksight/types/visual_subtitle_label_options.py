"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualSubtitleLabelOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.long_format_text
    import capo_quicksight.types.visibility


class VisualSubtitleLabelOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the subtitle label.</p>"""
    format_text: NotRequired["capo_quicksight.types.long_format_text.LongFormatText"]
    """<p>The long text format of the subtitle label, such as plain text or rich text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualSubtitleLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "format_text" in value:
        import capo_quicksight.types.long_format_text

        out["FormatText"] = capo_quicksight.types.long_format_text.serialize_json(
            value["format_text"]
        )
    return out


def deserialize_json(data: dict) -> VisualSubtitleLabelOptions:
    out: VisualSubtitleLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "FormatText" in data:
        import capo_quicksight.types.long_format_text

        out["format_text"] = capo_quicksight.types.long_format_text.deserialize_json(
            data["FormatText"]
        )
    return out
