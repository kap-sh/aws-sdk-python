"""Generated from Smithy shape ``com.amazonaws.lakeformation#RowFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.all_rows_wildcard
    import aws_sdk_lakeformation.types.predicate_string


class RowFilter(TypedDict, closed=True):
    filter_expression: NotRequired[
        "aws_sdk_lakeformation.types.predicate_string.PredicateString"
    ]
    """<p>A filter expression.</p>"""
    all_rows_wildcard: NotRequired[
        "aws_sdk_lakeformation.types.all_rows_wildcard.AllRowsWildcard"
    ]
    """<p>A wildcard for all rows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowFilter) -> dict:
    out: dict = {}
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    if "all_rows_wildcard" in value:
        import aws_sdk_lakeformation.types.all_rows_wildcard

        out["AllRowsWildcard"] = (
            aws_sdk_lakeformation.types.all_rows_wildcard.serialize_json(
                value["all_rows_wildcard"]
            )
        )
    return out


def deserialize_json(data: dict) -> RowFilter:
    out: RowFilter = {}  # type: ignore[typeddict-item]
    if "FilterExpression" in data:
        out["filter_expression"] = data["FilterExpression"]
    if "AllRowsWildcard" in data:
        import aws_sdk_lakeformation.types.all_rows_wildcard

        out["all_rows_wildcard"] = (
            aws_sdk_lakeformation.types.all_rows_wildcard.deserialize_json(
                data["AllRowsWildcard"]
            )
        )
    return out
