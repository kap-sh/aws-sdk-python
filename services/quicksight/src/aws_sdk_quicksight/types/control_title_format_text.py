"""Generated from Smithy shape ``com.amazonaws.quicksight#ControlTitleFormatText``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.control_title_plain_text
    import aws_sdk_quicksight.types.control_title_rich_text


class ControlTitleFormatText(TypedDict, closed=True):
    plain_text: NotRequired[
        "aws_sdk_quicksight.types.control_title_plain_text.ControlTitlePlainText"
    ]
    """<p>The plain text format of the title text.</p>"""
    rich_text: NotRequired[
        "aws_sdk_quicksight.types.control_title_rich_text.ControlTitleRichText"
    ]
    """<p>The rich text format of the title text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlTitleFormatText) -> dict:
    out: dict = {}
    if "plain_text" in value:
        out["PlainText"] = value["plain_text"]
    if "rich_text" in value:
        out["RichText"] = value["rich_text"]
    return out


def deserialize_json(data: dict) -> ControlTitleFormatText:
    out: ControlTitleFormatText = {}  # type: ignore[typeddict-item]
    if "PlainText" in data:
        out["plain_text"] = data["PlainText"]
    if "RichText" in data:
        out["rich_text"] = data["RichText"]
    return out
