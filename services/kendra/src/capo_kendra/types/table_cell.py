"""Generated from Smithy shape ``com.amazonaws.kendra#TableCell``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.string


class TableCell(TypedDict, closed=True):
    value: NotRequired["capo_kendra.types.string.String"]
    """<p>The actual value or content within a table cell. A table cell could contain a date value of a year, or a string value of text, for example.</p>"""
    top_answer: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> if the response of the table cell is the top answer. This is the cell value or content with the highest confidence score or is the most relevant to the query.</p>"""
    highlighted: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> means that the table cell has a high enough confidence and is relevant to the query, so the value or content should be highlighted.</p>"""
    header: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> means that the table cell should be treated as a header.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableCell) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    out["TopAnswer"] = value.get("top_answer", False)
    out["Highlighted"] = value.get("highlighted", False)
    out["Header"] = value.get("header", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> TableCell:
    out: TableCell = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "TopAnswer" in data:
        out["top_answer"] = data["TopAnswer"]
    else:
        out["top_answer"] = False
    if "Highlighted" in data:
        out["highlighted"] = data["Highlighted"]
    else:
        out["highlighted"] = False
    if "Header" in data:
        out["header"] = data["Header"]
    else:
        out["header"] = False
    return out
