"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageTooltipText``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.long_plain_text


class SheetImageTooltipText(TypedDict, closed=True):
    plain_text: NotRequired["capo_quicksight.types.long_plain_text.LongPlainText"]
    """<p>The plain text format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageTooltipText) -> dict:
    out: dict = {}
    if "plain_text" in value:
        out["PlainText"] = value["plain_text"]
    return out


def deserialize_json(data: dict) -> SheetImageTooltipText:
    out: SheetImageTooltipText = {}  # type: ignore[typeddict-item]
    if "PlainText" in data:
        out["plain_text"] = data["PlainText"]
    return out
