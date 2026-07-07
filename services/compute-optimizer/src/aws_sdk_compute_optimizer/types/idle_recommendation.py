"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_id
    import aws_sdk_compute_optimizer.types.idle_finding
    import aws_sdk_compute_optimizer.types.idle_finding_description
    import aws_sdk_compute_optimizer.types.idle_recommendation_resource_type
    import aws_sdk_compute_optimizer.types.idle_savings_opportunity
    import aws_sdk_compute_optimizer.types.idle_savings_opportunity_after_discounts
    import aws_sdk_compute_optimizer.types.idle_utilization_metrics
    import aws_sdk_compute_optimizer.types.last_refresh_timestamp
    import aws_sdk_compute_optimizer.types.look_back_period_in_days
    import aws_sdk_compute_optimizer.types.resource_arn
    import aws_sdk_compute_optimizer.types.resource_id
    import aws_sdk_compute_optimizer.types.tags


class IdleRecommendation(TypedDict, closed=True):
    resource_arn: NotRequired[
        "aws_sdk_compute_optimizer.types.resource_arn.ResourceArn"
    ]
    """<p>The ARN of the current idle resource.</p>"""
    resource_id: NotRequired["aws_sdk_compute_optimizer.types.resource_id.ResourceId"]
    """<p>The unique identifier for the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_recommendation_resource_type.IdleRecommendationResourceType"
    ]
    """<p>The type of resource that is idle.</p>"""
    account_id: NotRequired["aws_sdk_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the idle resource.</p>"""
    finding: NotRequired["aws_sdk_compute_optimizer.types.idle_finding.IdleFinding"]
    """<p>The finding classification of an idle resource.</p>"""
    finding_description: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_finding_description.IdleFindingDescription"
    ]
    """<p>A summary of the findings for the resource.</p>"""
    savings_opportunity: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_savings_opportunity.IdleSavingsOpportunity"
    ]
    """<p>The savings opportunity for the idle resource.</p>"""
    savings_opportunity_after_discounts: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_savings_opportunity_after_discounts.IdleSavingsOpportunityAfterDiscounts"
    ]
    """<p>The savings opportunity for the idle resource after any applying discounts.</p>"""
    utilization_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_utilization_metrics.IdleUtilizationMetrics"
    ]
    """<p>An array of objects that describe the utilization metrics of the idle resource.</p>"""
    look_back_period_in_days: (
        "aws_sdk_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p>The number of days the idle resource utilization metrics were analyzed.</p>"""
    last_refresh_timestamp: NotRequired[
        "aws_sdk_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p>The timestamp of when the idle resource recommendation was last generated.</p>"""
    tags: NotRequired["aws_sdk_compute_optimizer.types.tags.Tags"]
    """<p>A list of tags assigned to your idle resource recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        import aws_sdk_compute_optimizer.types.idle_recommendation_resource_type

        out["resourceType"] = (
            aws_sdk_compute_optimizer.types.idle_recommendation_resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "finding" in value:
        import aws_sdk_compute_optimizer.types.idle_finding

        out["finding"] = (
            aws_sdk_compute_optimizer.types.idle_finding.serialize_aws_json_1_0(
                value["finding"]
            )
        )
    if "finding_description" in value:
        out["findingDescription"] = value["finding_description"]
    if "savings_opportunity" in value:
        import aws_sdk_compute_optimizer.types.idle_savings_opportunity

        out["savingsOpportunity"] = (
            aws_sdk_compute_optimizer.types.idle_savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import aws_sdk_compute_optimizer.types.idle_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            aws_sdk_compute_optimizer.types.idle_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "utilization_metrics" in value:
        import aws_sdk_compute_optimizer.types.idle_utilization_metrics

        out["utilizationMetrics"] = (
            aws_sdk_compute_optimizer.types.idle_utilization_metrics.serialize_aws_json_1_0(
                value["utilization_metrics"]
            )
        )
    out["lookBackPeriodInDays"] = value.get("look_back_period_in_days", 0)
    if "last_refresh_timestamp" in value:
        import aws_sdk_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            aws_sdk_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "tags" in value:
        import aws_sdk_compute_optimizer.types.tags

        out["tags"] = aws_sdk_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleRecommendation:
    out: IdleRecommendation = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        import aws_sdk_compute_optimizer.types.idle_recommendation_resource_type

        out["resource_type"] = (
            aws_sdk_compute_optimizer.types.idle_recommendation_resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "finding" in data:
        import aws_sdk_compute_optimizer.types.idle_finding

        out["finding"] = (
            aws_sdk_compute_optimizer.types.idle_finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if "findingDescription" in data:
        out["finding_description"] = data["findingDescription"]
    if "savingsOpportunity" in data:
        import aws_sdk_compute_optimizer.types.idle_savings_opportunity

        out["savings_opportunity"] = (
            aws_sdk_compute_optimizer.types.idle_savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if "savingsOpportunityAfterDiscounts" in data:
        import aws_sdk_compute_optimizer.types.idle_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            aws_sdk_compute_optimizer.types.idle_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if "utilizationMetrics" in data:
        import aws_sdk_compute_optimizer.types.idle_utilization_metrics

        out["utilization_metrics"] = (
            aws_sdk_compute_optimizer.types.idle_utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if "lookBackPeriodInDays" in data:
        out["look_back_period_in_days"] = data["lookBackPeriodInDays"]
    else:
        out["look_back_period_in_days"] = 0
    if "lastRefreshTimestamp" in data:
        import aws_sdk_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            aws_sdk_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if "tags" in data:
        import aws_sdk_compute_optimizer.types.tags

        out["tags"] = aws_sdk_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
