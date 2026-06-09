"""Generated from Smithy shape ``com.amazonaws.iam#Position``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.column_number
    import aws_sdk_iam.types.line_number


class Position(TypedDict):
    line: "aws_sdk_iam.types.line_number.LineNumber"
    """<p>The line containing the specified position in the document.</p>"""
    column: "aws_sdk_iam.types.column_number.ColumnNumber"
    """<p>The column in the line containing the specified position in the document.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Position, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((f"{prefix}.Line", str(value.get("line", 0))))
    pairs.append((f"{prefix}.Column", str(value.get("column", 0))))


def deserialize_query(el: Element) -> Position:
    out: Position = {}  # type: ignore[typeddict-item]
    child_line = el.find("Line")
    if child_line is not None:
        out["line"] = int(child_line.text or "")
    else:
        out["line"] = 0
    child_column = el.find("Column")
    if child_column is not None:
        out["column"] = int(child_column.text or "")
    else:
        out["column"] = 0
    return out
