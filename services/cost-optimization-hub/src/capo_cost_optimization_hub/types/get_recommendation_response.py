"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#GetRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.action_type
    import capo_cost_optimization_hub.types.datetime
    import capo_cost_optimization_hub.types.implementation_effort
    import capo_cost_optimization_hub.types.resource_details
    import capo_cost_optimization_hub.types.resource_type
    import capo_cost_optimization_hub.types.source
    import capo_cost_optimization_hub.types.tag_list


class GetRecommendationResponse(TypedDict, closed=True):
    recommendation_id: NotRequired["str"]
    """<p>The ID for the recommendation.</p>"""
    resource_id: NotRequired["str"]
    """<p>The unique identifier for the resource. This is the same as the Amazon Resource Name (ARN), if available.</p>"""
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    account_id: NotRequired["str"]
    """<p>The account to which the recommendation applies.</p>"""
    currency_code: NotRequired["str"]
    """<p>The currency code used for the recommendation.</p>"""
    recommendation_lookback_period_in_days: NotRequired["int"]
    """<p>The lookback period that's used to generate the recommendation.</p>"""
    cost_calculation_lookback_period_in_days: NotRequired["int"]
    """<p>The lookback period used to calculate cost impact for a recommendation.</p>"""
    estimated_savings_percentage: NotRequired["float"]
    """<p>The estimated savings percentage relative to the total cost over the cost calculation lookback period.</p>"""
    estimated_savings_over_cost_calculation_lookback_period: NotRequired["float"]
    """<p>The estimated savings amount over the lookback period used to calculate cost impact for a recommendation.</p>"""
    current_resource_type: NotRequired[
        "capo_cost_optimization_hub.types.resource_type.ResourceType"
    ]
    """<p>The type of resource.</p>"""
    recommended_resource_type: NotRequired[
        "capo_cost_optimization_hub.types.resource_type.ResourceType"
    ]
    """<p>The resource type of the recommendation.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    source: NotRequired["capo_cost_optimization_hub.types.source.Source"]
    """<p>The source of the recommendation.</p>"""
    last_refresh_timestamp: NotRequired[
        "capo_cost_optimization_hub.types.datetime.Datetime"
    ]
    """<p>The time when the recommendation was last generated.</p>"""
    estimated_monthly_savings: NotRequired["float"]
    """<p>The estimated monthly savings amount for the recommendation.</p>"""
    estimated_monthly_cost: NotRequired["float"]
    """<p>The estimated monthly cost of the current resource. For Reserved Instances and Savings Plans, it refers to the cost for eligible usage.</p>"""
    implementation_effort: NotRequired[
        "capo_cost_optimization_hub.types.implementation_effort.ImplementationEffort"
    ]
    """<p>The effort required to implement the recommendation.</p>"""
    restart_needed: NotRequired["bool"]
    """<p>Whether or not implementing the recommendation requires a restart.</p>"""
    action_type: NotRequired["capo_cost_optimization_hub.types.action_type.ActionType"]
    """<p>The type of action you can take by adopting the recommendation.</p>"""
    rollback_possible: NotRequired["bool"]
    """<p>Whether or not implementing the recommendation can be rolled back.</p>"""
    current_resource_details: NotRequired[
        "capo_cost_optimization_hub.types.resource_details.ResourceDetails"
    ]
    """<p>The details for the resource.</p>"""
    recommended_resource_details: NotRequired[
        "capo_cost_optimization_hub.types.resource_details.ResourceDetails"
    ]
    """<p>The details about the recommended resource.</p>"""
    tags: NotRequired["capo_cost_optimization_hub.types.tag_list.TagList"]
    """<p>A list of tags associated with the resource for which the recommendation exists.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationResponse) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "recommendation_lookback_period_in_days" in value:
        out["recommendationLookbackPeriodInDays"] = value[
            "recommendation_lookback_period_in_days"
        ]
    if "cost_calculation_lookback_period_in_days" in value:
        out["costCalculationLookbackPeriodInDays"] = value[
            "cost_calculation_lookback_period_in_days"
        ]
    if "estimated_savings_percentage" in value:
        out["estimatedSavingsPercentage"] = value["estimated_savings_percentage"]
    if "estimated_savings_over_cost_calculation_lookback_period" in value:
        out["estimatedSavingsOverCostCalculationLookbackPeriod"] = value[
            "estimated_savings_over_cost_calculation_lookback_period"
        ]
    if "current_resource_type" in value:
        import capo_cost_optimization_hub.types.resource_type

        out["currentResourceType"] = (
            capo_cost_optimization_hub.types.resource_type.serialize_aws_json_1_0(
                value["current_resource_type"]
            )
        )
    if "recommended_resource_type" in value:
        import capo_cost_optimization_hub.types.resource_type

        out["recommendedResourceType"] = (
            capo_cost_optimization_hub.types.resource_type.serialize_aws_json_1_0(
                value["recommended_resource_type"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "source" in value:
        import capo_cost_optimization_hub.types.source

        out["source"] = capo_cost_optimization_hub.types.source.serialize_aws_json_1_0(
            value["source"]
        )
    if "last_refresh_timestamp" in value:
        import capo_cost_optimization_hub.types.datetime

        out["lastRefreshTimestamp"] = (
            capo_cost_optimization_hub.types.datetime.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "estimated_monthly_savings" in value:
        out["estimatedMonthlySavings"] = value["estimated_monthly_savings"]
    if "estimated_monthly_cost" in value:
        out["estimatedMonthlyCost"] = value["estimated_monthly_cost"]
    if "implementation_effort" in value:
        import capo_cost_optimization_hub.types.implementation_effort

        out["implementationEffort"] = (
            capo_cost_optimization_hub.types.implementation_effort.serialize_aws_json_1_0(
                value["implementation_effort"]
            )
        )
    if "restart_needed" in value:
        out["restartNeeded"] = value["restart_needed"]
    if "action_type" in value:
        import capo_cost_optimization_hub.types.action_type

        out["actionType"] = (
            capo_cost_optimization_hub.types.action_type.serialize_aws_json_1_0(
                value["action_type"]
            )
        )
    if "rollback_possible" in value:
        out["rollbackPossible"] = value["rollback_possible"]
    if "current_resource_details" in value:
        import capo_cost_optimization_hub.types.resource_details

        out["currentResourceDetails"] = (
            capo_cost_optimization_hub.types.resource_details.serialize_aws_json_1_0(
                value["current_resource_details"]
            )
        )
    if "recommended_resource_details" in value:
        import capo_cost_optimization_hub.types.resource_details

        out["recommendedResourceDetails"] = (
            capo_cost_optimization_hub.types.resource_details.serialize_aws_json_1_0(
                value["recommended_resource_details"]
            )
        )
    if "tags" in value:
        import capo_cost_optimization_hub.types.tag_list

        out["tags"] = capo_cost_optimization_hub.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationResponse:
    out: GetRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "recommendationLookbackPeriodInDays" in data:
        out["recommendation_lookback_period_in_days"] = data[
            "recommendationLookbackPeriodInDays"
        ]
    if "costCalculationLookbackPeriodInDays" in data:
        out["cost_calculation_lookback_period_in_days"] = data[
            "costCalculationLookbackPeriodInDays"
        ]
    if "estimatedSavingsPercentage" in data:
        out["estimated_savings_percentage"] = data["estimatedSavingsPercentage"]
    if "estimatedSavingsOverCostCalculationLookbackPeriod" in data:
        out["estimated_savings_over_cost_calculation_lookback_period"] = data[
            "estimatedSavingsOverCostCalculationLookbackPeriod"
        ]
    if "currentResourceType" in data:
        import capo_cost_optimization_hub.types.resource_type

        out["current_resource_type"] = (
            capo_cost_optimization_hub.types.resource_type.deserialize_aws_json_1_0(
                data["currentResourceType"]
            )
        )
    if "recommendedResourceType" in data:
        import capo_cost_optimization_hub.types.resource_type

        out["recommended_resource_type"] = (
            capo_cost_optimization_hub.types.resource_type.deserialize_aws_json_1_0(
                data["recommendedResourceType"]
            )
        )
    if "region" in data:
        out["region"] = data["region"]
    if "source" in data:
        import capo_cost_optimization_hub.types.source

        out["source"] = (
            capo_cost_optimization_hub.types.source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    if "lastRefreshTimestamp" in data:
        import capo_cost_optimization_hub.types.datetime

        out["last_refresh_timestamp"] = (
            capo_cost_optimization_hub.types.datetime.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if "estimatedMonthlySavings" in data:
        out["estimated_monthly_savings"] = data["estimatedMonthlySavings"]
    if "estimatedMonthlyCost" in data:
        out["estimated_monthly_cost"] = data["estimatedMonthlyCost"]
    if "implementationEffort" in data:
        import capo_cost_optimization_hub.types.implementation_effort

        out["implementation_effort"] = (
            capo_cost_optimization_hub.types.implementation_effort.deserialize_aws_json_1_0(
                data["implementationEffort"]
            )
        )
    if "restartNeeded" in data:
        out["restart_needed"] = data["restartNeeded"]
    if "actionType" in data:
        import capo_cost_optimization_hub.types.action_type

        out["action_type"] = (
            capo_cost_optimization_hub.types.action_type.deserialize_aws_json_1_0(
                data["actionType"]
            )
        )
    if "rollbackPossible" in data:
        out["rollback_possible"] = data["rollbackPossible"]
    if "currentResourceDetails" in data:
        import capo_cost_optimization_hub.types.resource_details

        out["current_resource_details"] = (
            capo_cost_optimization_hub.types.resource_details.deserialize_aws_json_1_0(
                data["currentResourceDetails"]
            )
        )
    if "recommendedResourceDetails" in data:
        import capo_cost_optimization_hub.types.resource_details

        out["recommended_resource_details"] = (
            capo_cost_optimization_hub.types.resource_details.deserialize_aws_json_1_0(
                data["recommendedResourceDetails"]
            )
        )
    if "tags" in data:
        import capo_cost_optimization_hub.types.tag_list

        out["tags"] = (
            capo_cost_optimization_hub.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
