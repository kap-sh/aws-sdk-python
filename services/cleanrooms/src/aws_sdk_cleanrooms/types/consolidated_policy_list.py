"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConsolidatedPolicyList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.additional_analyses
    import aws_sdk_cleanrooms.types.allowed_additional_analyses
    import aws_sdk_cleanrooms.types.allowed_result_receivers
    import aws_sdk_cleanrooms.types.analysis_rule_column_list
    import aws_sdk_cleanrooms.types.join_operators_list


class ConsolidatedPolicyList(TypedDict):
    join_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p> The columns to join on.</p>"""
    allowed_join_operators: NotRequired[
        "aws_sdk_cleanrooms.types.join_operators_list.JoinOperatorsList"
    ]
    """<p> The allowed join operators in the consolidated policy list.</p>"""
    list_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p> The columns in the consolidated policy list.</p>"""
    additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> Additional analyses for the consolidated policy list.</p>"""
    allowed_result_receivers: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_result_receivers.AllowedResultReceivers"
    ]
    """<p> The allowed result receivers.</p>"""
    allowed_additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_additional_analyses.AllowedAdditionalAnalyses"
    ]
    """<p> The additional analyses allowed by the consolidated policy list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedPolicyList) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_rule_column_list

    out["joinColumns"] = (
        aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["join_columns"]
        )
    )
    if "allowed_join_operators" in value:
        import aws_sdk_cleanrooms.types.join_operators_list

        out["allowedJoinOperators"] = (
            aws_sdk_cleanrooms.types.join_operators_list.serialize_json(
                value["allowed_join_operators"]
            )
        )
    import aws_sdk_cleanrooms.types.analysis_rule_column_list

    out["listColumns"] = (
        aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["list_columns"]
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


def deserialize_json(data: dict) -> ConsolidatedPolicyList:
    out: ConsolidatedPolicyList = {}  # type: ignore[typeddict-item]
    if "joinColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["join_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["joinColumns"]
            )
        )
    else:
        raise DeserializationError("ConsolidatedPolicyList.join_columns required")
    if "allowedJoinOperators" in data:
        import aws_sdk_cleanrooms.types.join_operators_list

        out["allowed_join_operators"] = (
            aws_sdk_cleanrooms.types.join_operators_list.deserialize_json(
                data["allowedJoinOperators"]
            )
        )
    if "listColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["list_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["listColumns"]
            )
        )
    else:
        raise DeserializationError("ConsolidatedPolicyList.list_columns required")
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
