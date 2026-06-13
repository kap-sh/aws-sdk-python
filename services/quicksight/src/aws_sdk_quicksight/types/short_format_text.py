"""Generated from Smithy shape ``com.amazonaws.quicksight#ShortFormatText``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_plain_text
    import aws_sdk_quicksight.types.short_rich_text


class ShortFormatText(TypedDict):
    plain_text: NotRequired["aws_sdk_quicksight.types.short_plain_text.ShortPlainText"]
    """<p>Plain text format.</p>"""
    rich_text: NotRequired["aws_sdk_quicksight.types.short_rich_text.ShortRichText"]
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
