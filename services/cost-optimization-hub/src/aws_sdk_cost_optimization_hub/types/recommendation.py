"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.datetime
    import aws_sdk_cost_optimization_hub.types.source
    import aws_sdk_cost_optimization_hub.types.tag_list


class Recommendation(TypedDict):
    recommendation_id: NotRequired["str"]
    """<p>The ID for the recommendation.</p>"""
    account_id: NotRequired["str"]
    """<p>The account to which the recommendation applies.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    resource_id: NotRequired["str"]
    """<p>The resource ID for the recommendation.</p>"""
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the recommendation.</p>"""
    current_resource_type: NotRequired["str"]
    """<p>The current resource type.</p>"""
    recommended_resource_type: NotRequired["str"]
    """<p>The recommended resource type.</p>"""
    estimated_monthly_savings: NotRequired["float"]
    """<p>The estimated monthly savings amount for the recommendation.</p>"""
    estimated_savings_percentage: NotRequired["float"]
    """<p>The estimated savings percentage relative to the total cost over the cost calculation lookback period.</p>"""
    estimated_monthly_cost: NotRequired["float"]
    """<p>The estimated monthly cost of the current resource. For Reserved Instances and Savings Plans, it refers to the cost for eligible usage.</p>"""
    currency_code: NotRequired["str"]
    """<p>The currency code used for the recommendation.</p>"""
    implementation_effort: NotRequired["str"]
    """<p>The effort required to implement the recommendation.</p>"""
    restart_needed: NotRequired["bool"]
    """<p>Whether or not implementing the recommendation requires a restart.</p>"""
    action_type: NotRequired["str"]
    """<p>The type of tasks that can be carried out by this action.</p>"""
    rollback_possible: NotRequired["bool"]
    """<p>Whether or not implementing the recommendation can be rolled back.</p>"""
    current_resource_summary: NotRequired["str"]
    """<p>Describes the current resource.</p>"""
    recommended_resource_summary: NotRequired["str"]
    """<p>Describes the recommended resource.</p>"""
    last_refresh_timestamp: NotRequired[
        "aws_sdk_cost_optimization_hub.types.datetime.Datetime"
    ]
    """<p>The time when the recommendation was last generated.</p>"""
    recommendation_lookback_period_in_days: NotRequired["int"]
    """<p>The lookback period that's used to generate the recommendation.</p>"""
    source: NotRequired["aws_sdk_cost_optimization_hub.types.source.Source"]
    """<p>The source of the recommendation.</p>"""
    tags: NotRequired["aws_sdk_cost_optimization_hub.types.tag_list.TagList"]
    """<p>A list of tags assigned to the recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Recommendation) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "current_resource_type" in value:
        out["currentResourceType"] = value["current_resource_type"]
    if "recommended_resource_type" in value:
        out["recommendedResourceType"] = value["recommended_resource_type"]
    if "estimated_monthly_savings" in value:
        out["estimatedMonthlySavings"] = value["estimated_monthly_savings"]
    if "estimated_savings_percentage" in value:
        out["estimatedSavingsPercentage"] = value["estimated_savings_percentage"]
    if "estimated_monthly_cost" in value:
        out["estimatedMonthlyCost"] = value["estimated_monthly_cost"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "implementation_effort" in value:
        out["implementationEffort"] = value["implementation_effort"]
    if "restart_needed" in value:
        out["restartNeeded"] = value["restart_needed"]
    if "action_type" in value:
        out["actionType"] = value["action_type"]
    if "rollback_possible" in value:
        out["rollbackPossible"] = value["rollback_possible"]
    if "current_resource_summary" in value:
        out["currentResourceSummary"] = value["current_resource_summary"]
    if "recommended_resource_summary" in value:
        out["recommendedResourceSummary"] = value["recommended_resource_summary"]
    if "last_refresh_timestamp" in value:
        import aws_sdk_cost_optimization_hub.types.datetime

        out["lastRefreshTimestamp"] = (
            aws_sdk_cost_optimization_hub.types.datetime.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "recommendation_lookback_period_in_days" in value:
        out["recommendationLookbackPeriodInDays"] = value[
            "recommendation_lookback_period_in_days"
        ]
    if "source" in value:
        import aws_sdk_cost_optimization_hub.types.source

        out["source"] = (
            aws_sdk_cost_optimization_hub.types.source.serialize_aws_json_1_0(
                value["source"]
            )
        )
    if "tags" in value:
        import aws_sdk_cost_optimization_hub.types.tag_list

        out["tags"] = (
            aws_sdk_cost_optimization_hub.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "region" in data:
        out["region"] = data["region"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "currentResourceType" in data:
        out["current_resource_type"] = data["currentResourceType"]
    if "recommendedResourceType" in data:
        out["recommended_resource_type"] = data["recommendedResourceType"]
    if "estimatedMonthlySavings" in data:
        out["estimated_monthly_savings"] = data["estimatedMonthlySavings"]
    if "estimatedSavingsPercentage" in data:
        out["estimated_savings_percentage"] = data["estimatedSavingsPercentage"]
    if "estimatedMonthlyCost" in data:
        out["estimated_monthly_cost"] = data["estimatedMonthlyCost"]
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "implementationEffort" in data:
        out["implementation_effort"] = data["implementationEffort"]
    if "restartNeeded" in data:
        out["restart_needed"] = data["restartNeeded"]
    if "actionType" in data:
        out["action_type"] = data["actionType"]
    if "rollbackPossible" in data:
        out["rollback_possible"] = data["rollbackPossible"]
    if "currentResourceSummary" in data:
        out["current_resource_summary"] = data["currentResourceSummary"]
    if "recommendedResourceSummary" in data:
        out["recommended_resource_summary"] = data["recommendedResourceSummary"]
    if "lastRefreshTimestamp" in data:
        import aws_sdk_cost_optimization_hub.types.datetime

        out["last_refresh_timestamp"] = (
            aws_sdk_cost_optimization_hub.types.datetime.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if "recommendationLookbackPeriodInDays" in data:
        out["recommendation_lookback_period_in_days"] = data[
            "recommendationLookbackPeriodInDays"
        ]
    if "source" in data:
        import aws_sdk_cost_optimization_hub.types.source

        out["source"] = (
            aws_sdk_cost_optimization_hub.types.source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    if "tags" in data:
        import aws_sdk_cost_optimization_hub.types.tag_list

        out["tags"] = (
            aws_sdk_cost_optimization_hub.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
