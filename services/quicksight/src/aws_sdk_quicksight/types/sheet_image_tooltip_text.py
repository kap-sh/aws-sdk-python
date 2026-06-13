"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageTooltipText``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.long_plain_text


class SheetImageTooltipText(TypedDict):
    plain_text: NotRequired["aws_sdk_quicksight.types.long_plain_text.LongPlainText"]
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
