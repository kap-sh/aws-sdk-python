"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConsolidatedPolicyAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.additional_analyses
    import aws_sdk_cleanrooms.types.aggregate_column_list
    import aws_sdk_cleanrooms.types.aggregation_constraints
    import aws_sdk_cleanrooms.types.allowed_additional_analyses
    import aws_sdk_cleanrooms.types.allowed_result_receivers
    import aws_sdk_cleanrooms.types.analysis_rule_column_list
    import aws_sdk_cleanrooms.types.join_operators_list
    import aws_sdk_cleanrooms.types.join_required_option
    import aws_sdk_cleanrooms.types.scalar_functions_list


class ConsolidatedPolicyAggregation(TypedDict):
    aggregate_columns: (
        "aws_sdk_cleanrooms.types.aggregate_column_list.AggregateColumnList"
    )
    """<p> Aggregate columns in consolidated policy aggregation.</p>"""
    join_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p> The columns to join on.</p>"""
    join_required: NotRequired[
        "aws_sdk_cleanrooms.types.join_required_option.JoinRequiredOption"
    ]
    """<p> Join required</p>"""
    allowed_join_operators: NotRequired[
        "aws_sdk_cleanrooms.types.join_operators_list.JoinOperatorsList"
    ]
    """<p> The allowed join operators.</p>"""
    dimension_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p> The dimension columns of the consolidated policy aggregation.</p>"""
    scalar_functions: (
        "aws_sdk_cleanrooms.types.scalar_functions_list.ScalarFunctionsList"
    )
    """<p> The scalar functions.</p>"""
    output_constraints: (
        "aws_sdk_cleanrooms.types.aggregation_constraints.AggregationConstraints"
    )
    """<p> The output constraints of the consolidated policy aggregation.</p>"""
    additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> Additional analyses for the consolidated policy aggregation.</p>"""
    allowed_result_receivers: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_result_receivers.AllowedResultReceivers"
    ]
    """<p> The allowed result receivers.</p>"""
    allowed_additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_additional_analyses.AllowedAdditionalAnalyses"
    ]
    """<p> The additional analyses allowed by the consolidated policy aggregation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedPolicyAggregation) -> dict:
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
    if "allowed_result_receivers" in value:
        import aws_sdk_cleanrooms.types.allowed_result_receivers

        out["allowedResultReceivers"] = (
            aws_sdk_cleanrooms.types.allowed_result_receivers.serialize_json(
                value["allowed_result_receivers"]
            )
        )
    if "allowed_additional_analyses" in value:
        import aws_sdk_cleanrooms.types.allowed_additional_analyses

        out["allowedAdditionalAnalyses"] = (
            aws_sdk_cleanrooms.types.allowed_additional_analyses.serialize_json(
                value["allowed_additional_analyses"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConsolidatedPolicyAggregation:
    out: ConsolidatedPolicyAggregation = {}  # type: ignore[typeddict-item]
    if "aggregateColumns" in data:
        import aws_sdk_cleanrooms.types.aggregate_column_list

        out["aggregate_columns"] = (
            aws_sdk_cleanrooms.types.aggregate_column_list.deserialize_json(
                data["aggregateColumns"]
            )
        )
    else:
        raise DeserializationError(
            "ConsolidatedPolicyAggregation.aggregate_columns required"
        )
    if "joinColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["join_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["joinColumns"]
            )
        )
    else:
        raise DeserializationError(
            "ConsolidatedPolicyAggregation.join_columns required"
        )
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
        raise DeserializationError(
            "ConsolidatedPolicyAggregation.dimension_columns required"
        )
    if "scalarFunctions" in data:
        import aws_sdk_cleanrooms.types.scalar_functions_list

        out["scalar_functions"] = (
            aws_sdk_cleanrooms.types.scalar_functions_list.deserialize_json(
                data["scalarFunctions"]
            )
        )
    else:
        raise DeserializationError(
            "ConsolidatedPolicyAggregation.scalar_functions required"
        )
    if "outputConstraints" in data:
        import aws_sdk_cleanrooms.types.aggregation_constraints

        out["output_constraints"] = (
            aws_sdk_cleanrooms.types.aggregation_constraints.deserialize_json(
                data["outputConstraints"]
            )
        )
    else:
        raise DeserializationError(
            "ConsolidatedPolicyAggregation.output_constraints required"
        )
    if "additionalAnalyses" in data:
        import aws_sdk_cleanrooms.types.additional_analyses

        out["additional_analyses"] = (
            aws_sdk_cleanrooms.types.additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    if "allowedResultReceivers" in data:
        import aws_sdk_cleanrooms.types.allowed_result_receivers

        out["allowed_result_receivers"] = (
            aws_sdk_cleanrooms.types.allowed_result_receivers.deserialize_json(
                data["allowedResultReceivers"]
            )
        )
    if "allowedAdditionalAnalyses" in data:
        import aws_sdk_cleanrooms.types.allowed_additional_analyses

        out["allowed_additional_analyses"] = (
            aws_sdk_cleanrooms.types.allowed_additional_analyses.deserialize_json(
                data["allowedAdditionalAnalyses"]
            )
        )
    return out
