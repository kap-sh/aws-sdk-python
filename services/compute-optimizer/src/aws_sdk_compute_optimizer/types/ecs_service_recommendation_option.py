"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.container_recommendations
    import aws_sdk_compute_optimizer.types.ecs_savings_opportunity_after_discounts
    import aws_sdk_compute_optimizer.types.ecs_service_projected_utilization_metrics
    import aws_sdk_compute_optimizer.types.nullable_cpu
    import aws_sdk_compute_optimizer.types.nullable_memory
    import aws_sdk_compute_optimizer.types.savings_opportunity


class ECSServiceRecommendationOption(TypedDict, closed=True):
    memory: NotRequired[
        "aws_sdk_compute_optimizer.types.nullable_memory.NullableMemory"
    ]
    """<p> The memory size of the Amazon ECS service recommendation option. </p>"""
    cpu: NotRequired["aws_sdk_compute_optimizer.types.nullable_cpu.NullableCpu"]
    """<p> The CPU size of the Amazon ECS service recommendation option. </p>"""
    savings_opportunity: NotRequired[
        "aws_sdk_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    savings_opportunity_after_discounts: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_savings_opportunity_after_discounts.ECSSavingsOpportunityAfterDiscounts"
    ]
    """<p> Describes the savings opportunity for Amazon ECS service recommendations or for the recommendation option. </p> <p>Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.</p>"""
    projected_utilization_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_projected_utilization_metrics.ECSServiceProjectedUtilizationMetrics"
    ]
    """<p> An array of objects that describe the projected utilization metrics of the Amazon ECS service recommendation option. </p>"""
    container_recommendations: NotRequired[
        "aws_sdk_compute_optimizer.types.container_recommendations.ContainerRecommendations"
    ]
    """<p> The CPU and memory size recommendations for the containers within the task of your Amazon ECS service. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendationOption) -> dict:
    out: dict = {}
    if "memory" in value:
        out["memory"] = value["memory"]
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "savings_opportunity" in value:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import aws_sdk_compute_optimizer.types.ecs_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            aws_sdk_compute_optimizer.types.ecs_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "projected_utilization_metrics" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_projected_utilization_metrics

        out["projectedUtilizationMetrics"] = (
            aws_sdk_compute_optimizer.types.ecs_service_projected_utilization_metrics.serialize_aws_json_1_0(
                value["projected_utilization_metrics"]
            )
        )
    if "container_recommendations" in value:
        import aws_sdk_compute_optimizer.types.container_recommendations

        out["containerRecommendations"] = (
            aws_sdk_compute_optimizer.types.container_recommendations.serialize_aws_json_1_0(
                value["container_recommendations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSServiceRecommendationOption:
    out: ECSServiceRecommendationOption = {}  # type: ignore[typeddict-item]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    if "savingsOpportunity" in data:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if "savingsOpportunityAfterDiscounts" in data:
        import aws_sdk_compute_optimizer.types.ecs_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            aws_sdk_compute_optimizer.types.ecs_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if "projectedUtilizationMetrics" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_projected_utilization_metrics

        out["projected_utilization_metrics"] = (
            aws_sdk_compute_optimizer.types.ecs_service_projected_utilization_metrics.deserialize_aws_json_1_0(
                data["projectedUtilizationMetrics"]
            )
        )
    if "containerRecommendations" in data:
        import aws_sdk_compute_optimizer.types.container_recommendations

        out["container_recommendations"] = (
            aws_sdk_compute_optimizer.types.container_recommendations.deserialize_aws_json_1_0(
                data["containerRecommendations"]
            )
        )
    return out
