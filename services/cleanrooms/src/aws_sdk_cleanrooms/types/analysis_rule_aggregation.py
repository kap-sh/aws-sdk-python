"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.additional_analyses
    import aws_sdk_cleanrooms.types.aggregate_column_list
    import aws_sdk_cleanrooms.types.aggregation_constraints
    import aws_sdk_cleanrooms.types.analysis_rule_column_list
    import aws_sdk_cleanrooms.types.join_operators_list
    import aws_sdk_cleanrooms.types.join_required_option
    import aws_sdk_cleanrooms.types.scalar_functions_list


class AnalysisRuleAggregation(TypedDict):
    aggregate_columns: (
        "aws_sdk_cleanrooms.types.aggregate_column_list.AggregateColumnList"
    )
    """<p>The columns that query runners are allowed to use in aggregation queries.</p>"""
    join_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>Columns in configured table that can be used in join statements and/or as aggregate columns. They can never be outputted directly.</p>"""
    join_required: NotRequired[
        "aws_sdk_cleanrooms.types.join_required_option.JoinRequiredOption"
    ]
    """<p>Control that requires member who runs query to do a join with their configured table and/or other configured table in query.</p>"""
    allowed_join_operators: NotRequired[
        "aws_sdk_cleanrooms.types.join_operators_list.JoinOperatorsList"
    ]
    """<p>Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is <code>AND</code>.</p>"""
    dimension_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>The columns that query runners are allowed to select, group by, or filter by.</p>"""
    scalar_functions: (
        "aws_sdk_cleanrooms.types.scalar_functions_list.ScalarFunctionsList"
    )
    """<p>Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.</p>"""
    output_constraints: (
        "aws_sdk_cleanrooms.types.aggregation_constraints.AggregationConstraints"
    )
    """<p>Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.</p>"""
    additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query. </p> <p>The <code>additionalAnalyses</code> parameter is currently supported for the list analysis rule (<code>AnalysisRuleList</code>) and the custom analysis rule (<code>AnalysisRuleCustom</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleAggregation) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.aggregate_column_list

    out["aggregateColumns"] = (
        aws_sdk_cleanrooms.types.aggregate_column_list.serialize_json(
            value["aggregate_columns"]
        )
    )
    import aws_sdk_cleanrooms.types.analysis_rule_column_list

    out["joinColumns"] = (
        aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["join_columns"]
        )
    )
    if "join_required" in value:
        out["joinRequired"] = value["join_required"]
    if "allowed_join_operators" in value:
        import aws_sdk_cleanrooms.types.join_operators_list

        out["allowedJoinOperators"] = (
            aws_sdk_cleanrooms.types.join_operators_list.serialize_json(
                value["allowed_join_operators"]
            )
        )
    import aws_sdk_cleanrooms.types.analysis_rule_column_list

    out["dimensionColumns"] = (
        aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["dimension_columns"]
        )
    )
    import aws_sdk_cleanrooms.types.scalar_functions_list

    out["scalarFunctions"] = (
        aws_sdk_cleanrooms.types.scalar_functions_list.serialize_json(
            value["scalar_functions"]
        )
    )
    import aws_sdk_cleanrooms.types.aggregation_constraints

    out["outputConstraints"] = (
        aws_sdk_cleanrooms.types.aggregation_constraints.serialize_json(
            value["output_constraints"]
        )
    )
    if "additional_analyses" in value:
        import aws_sdk_cleanrooms.types.additional_analyses

        out["additionalAnalyses"] = (
            aws_sdk_cleanrooms.types.additional_analyses.serialize_json(
                value["additional_analyses"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleAggregation:
    out: AnalysisRuleAggregation = {}  # type: ignore[typeddict-item]
    if "aggregateColumns" in data:
        import aws_sdk_cleanrooms.types.aggregate_column_list

        out["aggregate_columns"] = (
            aws_sdk_cleanrooms.types.aggregate_column_list.deserialize_json(
                data["aggregateColumns"]
            )
        )
    else:
        raise DeserializationError("AnalysisRuleAggregation.aggregate_columns required")
    if "joinColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["join_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["joinColumns"]
            )
        )
    else:
        raise DeserializationError("AnalysisRuleAggregation.join_columns required")
    if "joinRequired" in data:
        out["join_required"] = data["joinRequired"]
    if "allowedJoinOperators" in data:
        import aws_sdk_cleanrooms.types.join_operators_list

        out["allowed_join_operators"] = (
            aws_sdk_cleanrooms.types.join_operators_list.deserialize_json(
                data["allowedJoinOperators"]
            )
        )
    if "dimensionColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["dimension_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["dimensionColumns"]
            )
        )
    else:
        raise DeserializationError("AnalysisRuleAggregation.dimension_columns required")
    if "scalarFunctions" in data:
        import aws_sdk_cleanrooms.types.scalar_functions_list

        out["scalar_functions"] = (
            aws_sdk_cleanrooms.types.scalar_functions_list.deserialize_json(
                data["scalarFunctions"]
            )
        )
    else:
        raise DeserializationError("AnalysisRuleAggregation.scalar_functions required")
    if "outputConstraints" in data:
        import aws_sdk_cleanrooms.types.aggregation_constraints

        out["output_constraints"] = (
            aws_sdk_cleanrooms.types.aggregation_constraints.deserialize_json(
                data["outputConstraints"]
            )
        )
    else:
        raise DeserializationError(
            "AnalysisRuleAggregation.output_constraints required"
        )
    if "additionalAnalyses" in data:
        import aws_sdk_cleanrooms.types.additional_analyses

        out["additional_analyses"] = (
            aws_sdk_cleanrooms.types.additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    return out
