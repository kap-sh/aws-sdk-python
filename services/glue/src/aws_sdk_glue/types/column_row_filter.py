"""Generated from Smithy shape ``com.amazonaws.glue#ColumnRowFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.predicate_string


class ColumnRowFilter(TypedDict):
    column_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>A string containing the name of the column.</p>"""
    row_filter_expression: NotRequired[
        "aws_sdk_glue.types.predicate_string.PredicateString"
    ]
    """<p>A string containing the row-level filter expression.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnRowFilter) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "row_filter_expression" in value:
        out["RowFilterExpression"] = value["row_filter_expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnRowFilter:
    out: ColumnRowFilter = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    if "RowFilterExpression" in data:
        out["row_filter_expression"] = data["RowFilterExpression"]
    return out
