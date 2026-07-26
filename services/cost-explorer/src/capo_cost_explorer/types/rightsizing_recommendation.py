"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.current_instance
    import capo_cost_explorer.types.finding_reason_codes
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.modify_recommendation_detail
    import capo_cost_explorer.types.rightsizing_type
    import capo_cost_explorer.types.terminate_recommendation_detail


class RightsizingRecommendation(TypedDict, closed=True):
    account_id: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The account that this recommendation is for.</p>"""
    current_instance: NotRequired[
        "capo_cost_explorer.types.current_instance.CurrentInstance"
    ]
    """<p>Context regarding the current instance.</p>"""
    rightsizing_type: NotRequired[
        "capo_cost_explorer.types.rightsizing_type.RightsizingType"
    ]
    """<p>A recommendation to either terminate or modify the resource.</p>"""
    modify_recommendation_detail: NotRequired[
        "capo_cost_explorer.types.modify_recommendation_detail.ModifyRecommendationDetail"
    ]
    """<p>The details for the modification recommendations. </p>"""
    terminate_recommendation_detail: NotRequired[
        "capo_cost_explorer.types.terminate_recommendation_detail.TerminateRecommendationDetail"
    ]
    """<p>The details for termination recommendations.</p>"""
    finding_reason_codes: NotRequired[
        "capo_cost_explorer.types.finding_reason_codes.FindingReasonCodes"
    ]
    """<p>The list of possible reasons why the recommendation is generated, such as under- or over-utilization of specific metrics (for example, CPU, Memory, Network). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RightsizingRecommendation) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "current_instance" in value:
        import capo_cost_explorer.types.current_instance

        out["CurrentInstance"] = (
            capo_cost_explorer.types.current_instance.serialize_aws_json_1_1(
                value["current_instance"]
            )
        )
    if "rightsizing_type" in value:
        import capo_cost_explorer.types.rightsizing_type

        out["RightsizingType"] = (
            capo_cost_explorer.types.rightsizing_type.serialize_aws_json_1_1(
                value["rightsizing_type"]
            )
        )
    if "modify_recommendation_detail" in value:
        import capo_cost_explorer.types.modify_recommendation_detail

        out["ModifyRecommendationDetail"] = (
            capo_cost_explorer.types.modify_recommendation_detail.serialize_aws_json_1_1(
                value["modify_recommendation_detail"]
            )
        )
    if "terminate_recommendation_detail" in value:
        import capo_cost_explorer.types.terminate_recommendation_detail

        out["TerminateRecommendationDetail"] = (
            capo_cost_explorer.types.terminate_recommendation_detail.serialize_aws_json_1_1(
                value["terminate_recommendation_detail"]
            )
        )
    if "finding_reason_codes" in value:
        import capo_cost_explorer.types.finding_reason_codes

        out["FindingReasonCodes"] = (
            capo_cost_explorer.types.finding_reason_codes.serialize_aws_json_1_1(
                value["finding_reason_codes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RightsizingRecommendation:
    out: RightsizingRecommendation = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CurrentInstance" in data:
        import capo_cost_explorer.types.current_instance

        out["current_instance"] = (
            capo_cost_explorer.types.current_instance.deserialize_aws_json_1_1(
                data["CurrentInstance"]
            )
        )
    if "RightsizingType" in data:
        import capo_cost_explorer.types.rightsizing_type

        out["rightsizing_type"] = (
            capo_cost_explorer.types.rightsizing_type.deserialize_aws_json_1_1(
                data["RightsizingType"]
            )
        )
    if "ModifyRecommendationDetail" in data:
        import capo_cost_explorer.types.modify_recommendation_detail

        out["modify_recommendation_detail"] = (
            capo_cost_explorer.types.modify_recommendation_detail.deserialize_aws_json_1_1(
                data["ModifyRecommendationDetail"]
            )
        )
    if "TerminateRecommendationDetail" in data:
        import capo_cost_explorer.types.terminate_recommendation_detail

        out["terminate_recommendation_detail"] = (
            capo_cost_explorer.types.terminate_recommendation_detail.deserialize_aws_json_1_1(
                data["TerminateRecommendationDetail"]
            )
        )
    if "FindingReasonCodes" in data:
        import capo_cost_explorer.types.finding_reason_codes

        out["finding_reason_codes"] = (
            capo_cost_explorer.types.finding_reason_codes.deserialize_aws_json_1_1(
                data["FindingReasonCodes"]
            )
        )
    return out
