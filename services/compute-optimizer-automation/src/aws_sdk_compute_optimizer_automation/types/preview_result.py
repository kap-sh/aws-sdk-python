"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#PreviewResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.account_id
    import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings
    import aws_sdk_compute_optimizer_automation.types.recommended_action_id
    import aws_sdk_compute_optimizer_automation.types.recommended_action_type
    import aws_sdk_compute_optimizer_automation.types.resource_arn
    import aws_sdk_compute_optimizer_automation.types.resource_details
    import aws_sdk_compute_optimizer_automation.types.resource_id
    import aws_sdk_compute_optimizer_automation.types.resource_type
    import aws_sdk_compute_optimizer_automation.types.tag_list


class PreviewResult(TypedDict, closed=True):
    recommended_action_id: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_action_id.RecommendedActionId"
    ]
    """<p>The ID of the recommended action being previewed.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource affected by the recommended action.</p>"""
    resource_id: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_id.ResourceId"
    ]
    """<p>The ID of the resource affected by the recommended action.</p>"""
    account_id: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID associated with the resource.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region where the resource is located.</p>"""
    resource_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_type.ResourceType"
    ]
    """<p>The type of resource being evaluated.</p>"""
    look_back_period_in_days: NotRequired["int"]
    """<p>The number of days of historical data used to analyze the resource.</p>"""
    recommended_action_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_action_type.RecommendedActionType"
    ]
    """<p>The type of recommended action being previewed.</p>"""
    current_resource_summary: NotRequired["str"]
    """<p>A summary of the resource's current configuration.</p>"""
    current_resource_details: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_details.ResourceDetails"
    ]
    recommended_resource_summary: NotRequired["str"]
    """<p>A summary of the resource's recommended configuration.</p>"""
    recommended_resource_details: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_details.ResourceDetails"
    ]
    restart_needed: NotRequired["bool"]
    """<p>Indicates whether implementing the recommended action requires a resource restart.</p>"""
    estimated_monthly_savings: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"
    ]
    resource_tags: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.tag_list.TagList"
    ]
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreviewResult) -> dict:
    out: dict = {}
    if "recommended_action_id" in value:
        out["recommendedActionId"] = value["recommended_action_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "resource_type" in value:
        import aws_sdk_compute_optimizer_automation.types.resource_type

        out["resourceType"] = (
            aws_sdk_compute_optimizer_automation.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "look_back_period_in_days" in value:
        out["lookBackPeriodInDays"] = value["look_back_period_in_days"]
    if "recommended_action_type" in value:
        import aws_sdk_compute_optimizer_automation.types.recommended_action_type

        out["recommendedActionType"] = (
            aws_sdk_compute_optimizer_automation.types.recommended_action_type.serialize_aws_json_1_0(
                value["recommended_action_type"]
            )
        )
    if "current_resource_summary" in value:
        out["currentResourceSummary"] = value["current_resource_summary"]
    if "current_resource_details" in value:
        import aws_sdk_compute_optimizer_automation.types.resource_details

        out["currentResourceDetails"] = (
            aws_sdk_compute_optimizer_automation.types.resource_details.serialize_aws_json_1_0(
                value["current_resource_details"]
            )
        )
    if "recommended_resource_summary" in value:
        out["recommendedResourceSummary"] = value["recommended_resource_summary"]
    if "recommended_resource_details" in value:
        import aws_sdk_compute_optimizer_automation.types.resource_details

        out["recommendedResourceDetails"] = (
            aws_sdk_compute_optimizer_automation.types.resource_details.serialize_aws_json_1_0(
                value["recommended_resource_details"]
            )
        )
    if "restart_needed" in value:
        out["restartNeeded"] = value["restart_needed"]
    if "estimated_monthly_savings" in value:
        import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    if "resource_tags" in value:
        import aws_sdk_compute_optimizer_automation.types.tag_list

        out["resourceTags"] = (
            aws_sdk_compute_optimizer_automation.types.tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PreviewResult:
    out: PreviewResult = {}  # type: ignore[typeddict-item]
    if "recommendedActionId" in data:
        out["recommended_action_id"] = data["recommendedActionId"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "region" in data:
        out["region"] = data["region"]
    if "resourceType" in data:
        import aws_sdk_compute_optimizer_automation.types.resource_type

        out["resource_type"] = (
            aws_sdk_compute_optimizer_automation.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if "lookBackPeriodInDays" in data:
        out["look_back_period_in_days"] = data["lookBackPeriodInDays"]
    if "recommendedActionType" in data:
        import aws_sdk_compute_optimizer_automation.types.recommended_action_type

        out["recommended_action_type"] = (
            aws_sdk_compute_optimizer_automation.types.recommended_action_type.deserialize_aws_json_1_0(
                data["recommendedActionType"]
            )
        )
    if "currentResourceSummary" in data:
        out["current_resource_summary"] = data["currentResourceSummary"]
    if "currentResourceDetails" in data:
        import aws_sdk_compute_optimizer_automation.types.resource_details

        out["current_resource_details"] = (
            aws_sdk_compute_optimizer_automation.types.resource_details.deserialize_aws_json_1_0(
                data["currentResourceDetails"]
            )
        )
    if "recommendedResourceSummary" in data:
        out["recommended_resource_summary"] = data["recommendedResourceSummary"]
    if "recommendedResourceDetails" in data:
        import aws_sdk_compute_optimizer_automation.types.resource_details

        out["recommended_resource_details"] = (
            aws_sdk_compute_optimizer_automation.types.resource_details.deserialize_aws_json_1_0(
                data["recommendedResourceDetails"]
            )
        )
    if "restartNeeded" in data:
        out["restart_needed"] = data["restartNeeded"]
    if "estimatedMonthlySavings" in data:
        import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    if "resourceTags" in data:
        import aws_sdk_compute_optimizer_automation.types.tag_list

        out["resource_tags"] = (
            aws_sdk_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out
