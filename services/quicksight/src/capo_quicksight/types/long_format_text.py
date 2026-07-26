"""Generated from Smithy shape ``com.amazonaws.quicksight#LongFormatText``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.long_plain_text
    import capo_quicksight.types.long_rich_text


class LongFormatText(TypedDict, closed=True):
    plain_text: NotRequired["capo_quicksight.types.long_plain_text.LongPlainText"]
    """<p>Plain text format.</p>"""
    rich_text: NotRequired["capo_quicksight.types.long_rich_text.LongRichText"]
    """<p>Rich text. Examples of rich text include bold, underline, and italics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LongFormatText) -> dict:
    out: dict = {}
    if "plain_text" in value:
        out["PlainText"] = value["plain_text"]
    if "rich_text" in value:
        out["RichText"] = value["rich_text"]
    return out


def deserialize_json(data: dict) -> LongFormatText:
    out: LongFormatText = {}  # type: ignore[typeddict-item]
    if "PlainText" in data:
        out["plain_text"] = data["PlainText"]
    if "RichText" in data:
        out["rich_text"] = data["RichText"]
    return out
