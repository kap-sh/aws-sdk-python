"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.current_instance
    import aws_sdk_cost_explorer.types.finding_reason_codes
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.modify_recommendation_detail
    import aws_sdk_cost_explorer.types.rightsizing_type
    import aws_sdk_cost_explorer.types.terminate_recommendation_detail


class RightsizingRecommendation(TypedDict):
    account_id: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The account that this recommendation is for.</p>"""
    current_instance: NotRequired[
        "aws_sdk_cost_explorer.types.current_instance.CurrentInstance"
    ]
    """<p>Context regarding the current instance.</p>"""
    rightsizing_type: NotRequired[
        "aws_sdk_cost_explorer.types.rightsizing_type.RightsizingType"
    ]
    """<p>A recommendation to either terminate or modify the resource.</p>"""
    modify_recommendation_detail: NotRequired[
        "aws_sdk_cost_explorer.types.modify_recommendation_detail.ModifyRecommendationDetail"
    ]
    """<p>The details for the modification recommendations. </p>"""
    terminate_recommendation_detail: NotRequired[
        "aws_sdk_cost_explorer.types.terminate_recommendation_detail.TerminateRecommendationDetail"
    ]
    """<p>The details for termination recommendations.</p>"""
    finding_reason_codes: NotRequired[
        "aws_sdk_cost_explorer.types.finding_reason_codes.FindingReasonCodes"
    ]
    """<p>The list of possible reasons why the recommendation is generated, such as under- or over-utilization of specific metrics (for example, CPU, Memory, Network). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RightsizingRecommendation) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "current_instance" in value:
        import aws_sdk_cost_explorer.types.current_instance

        out["CurrentInstance"] = (
            aws_sdk_cost_explorer.types.current_instance.serialize_aws_json_1_1(
                value["current_instance"]
            )
        )
    if "rightsizing_type" in value:
        import aws_sdk_cost_explorer.types.rightsizing_type

        out["RightsizingType"] = (
            aws_sdk_cost_explorer.types.rightsizing_type.serialize_aws_json_1_1(
                value["rightsizing_type"]
            )
        )
    if "modify_recommendation_detail" in value:
        import aws_sdk_cost_explorer.types.modify_recommendation_detail

        out["ModifyRecommendationDetail"] = (
            aws_sdk_cost_explorer.types.modify_recommendation_detail.serialize_aws_json_1_1(
                value["modify_recommendation_detail"]
            )
        )
    if "terminate_recommendation_detail" in value:
        import aws_sdk_cost_explorer.types.terminate_recommendation_detail

        out["TerminateRecommendationDetail"] = (
            aws_sdk_cost_explorer.types.terminate_recommendation_detail.serialize_aws_json_1_1(
                value["terminate_recommendation_detail"]
            )
        )
    if "finding_reason_codes" in value:
        import aws_sdk_cost_explorer.types.finding_reason_codes

        out["FindingReasonCodes"] = (
            aws_sdk_cost_explorer.types.finding_reason_codes.serialize_aws_json_1_1(
                value["finding_reason_codes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RightsizingRecommendation:
    out: RightsizingRecommendation = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CurrentInstance" in data:
        import aws_sdk_cost_explorer.types.current_instance

        out["current_instance"] = (
            aws_sdk_cost_explorer.types.current_instance.deserialize_aws_json_1_1(
                data["CurrentInstance"]
            )
        )
    if "RightsizingType" in data:
        import aws_sdk_cost_explorer.types.rightsizing_type

        out["rightsizing_type"] = (
            aws_sdk_cost_explorer.types.rightsizing_type.deserialize_aws_json_1_1(
                data["RightsizingType"]
            )
        )
    if "ModifyRecommendationDetail" in data:
        import aws_sdk_cost_explorer.types.modify_recommendation_detail

        out["modify_recommendation_detail"] = (
            aws_sdk_cost_explorer.types.modify_recommendation_detail.deserialize_aws_json_1_1(
                data["ModifyRecommendationDetail"]
            )
        )
    if "TerminateRecommendationDetail" in data:
        import aws_sdk_cost_explorer.types.terminate_recommendation_detail

        out["terminate_recommendation_detail"] = (
            aws_sdk_cost_explorer.types.terminate_recommendation_detail.deserialize_aws_json_1_1(
                data["TerminateRecommendationDetail"]
            )
        )
    if "FindingReasonCodes" in data:
        import aws_sdk_cost_explorer.types.finding_reason_codes

        out["finding_reason_codes"] = (
            aws_sdk_cost_explorer.types.finding_reason_codes.deserialize_aws_json_1_1(
                data["FindingReasonCodes"]
            )
        )
    return out
