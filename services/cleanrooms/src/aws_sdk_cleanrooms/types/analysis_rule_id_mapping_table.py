"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleIdMappingTable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_rule_column_list
    import aws_sdk_cleanrooms.types.query_constraint_list


class AnalysisRuleIdMappingTable(TypedDict):
    join_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>The columns that query runners are allowed to use in an INNER JOIN statement.</p>"""
    query_constraints: (
        "aws_sdk_cleanrooms.types.query_constraint_list.QueryConstraintList"
    )
    """<p>The query constraints of the analysis rule ID mapping table.</p>"""
    dimension_columns: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    ]
    """<p>The columns that query runners are allowed to select, group by, or filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleIdMappingTable) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_rule_column_list

    out["joinColumns"] = (
        aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["join_columns"]
        )
    )
    import aws_sdk_cleanrooms.types.query_constraint_list

    out["queryConstraints"] = (
        aws_sdk_cleanrooms.types.query_constraint_list.serialize_json(
            value["query_constraints"]
        )
    )
    if "dimension_columns" in value:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["dimensionColumns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
                value["dimension_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleIdMappingTable:
    out: AnalysisRuleIdMappingTable = {}  # type: ignore[typeddict-item]
    if "joinColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["join_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["joinColumns"]
            )
        )
    else:
        raise DeserializationError("AnalysisRuleIdMappingTable.join_columns required")
    if "queryConstraints" in data:
        import aws_sdk_cleanrooms.types.query_constraint_list

        out["query_constraints"] = (
            aws_sdk_cleanrooms.types.query_constraint_list.deserialize_json(
                data["queryConstraints"]
            )
        )
    else:
        raise DeserializationError(
            "AnalysisRuleIdMappingTable.query_constraints required"
        )
    if "dimensionColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["dimension_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["dimensionColumns"]
            )
        )
    return out
