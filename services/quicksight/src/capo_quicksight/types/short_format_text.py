"""Generated from Smithy shape ``com.amazonaws.quicksight#ShortFormatText``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.short_plain_text
    import capo_quicksight.types.short_rich_text


class ShortFormatText(TypedDict, closed=True):
    plain_text: NotRequired["capo_quicksight.types.short_plain_text.ShortPlainText"]
    """<p>Plain text format.</p>"""
    rich_text: NotRequired["capo_quicksight.types.short_rich_text.ShortRichText"]
    """<p>Rich text. Examples of rich text include bold, underline, and italics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShortFormatText) -> dict:
    out: dict = {}
    if "plain_text" in value:
        out["PlainText"] = value["plain_text"]
    if "rich_text" in value:
        out["RichText"] = value["rich_text"]
    return out


def deserialize_json(data: dict) -> ShortFormatText:
    out: ShortFormatText = {}  # type: ignore[typeddict-item]
    if "PlainText" in data:
        out["plain_text"] = data["PlainText"]
    if "RichText" in data:
        out["rich_text"] = data["RichText"]
    return out
