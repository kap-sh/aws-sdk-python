"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_descriptive_text


class ColumnDescription(TypedDict, closed=True):
    text: NotRequired[
        "aws_sdk_quicksight.types.column_descriptive_text.ColumnDescriptiveText"
    ]
    """<p>The text of a description for a column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnDescription) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    return out


def deserialize_json(data: dict) -> ColumnDescription:
    out: ColumnDescription = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    return out
