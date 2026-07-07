"""Generated from Smithy shape ``com.amazonaws.cleanrooms#QueryConstraintRequireOverlap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_rule_column_list


class QueryConstraintRequireOverlap(TypedDict, closed=True):
    columns: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    ]
    """<p>The columns that are required to overlap.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryConstraintRequireOverlap) -> dict:
    out: dict = {}
    if "columns" in value:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
                value["columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> QueryConstraintRequireOverlap:
    out: QueryConstraintRequireOverlap = {}  # type: ignore[typeddict-item]
    if "columns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["columns"]
            )
        )
    return out
