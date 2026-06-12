"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryRecommendationOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metrics
    import aws_sdk_compute_optimizer.types.lambda_savings_opportunity_after_discounts
    import aws_sdk_compute_optimizer.types.memory_size
    import aws_sdk_compute_optimizer.types.rank
    import aws_sdk_compute_optimizer.types.savings_opportunity


class LambdaFunctionMemoryRecommendationOption(TypedDict):
    rank: "aws_sdk_compute_optimizer.types.rank.Rank"
    """<p>The rank of the function recommendation option.</p> <p>The top recommendation option is ranked as <code>1</code>.</p>"""
    memory_size: "aws_sdk_compute_optimizer.types.memory_size.MemorySize"
    """<p>The memory size, in MB, of the function recommendation option.</p>"""
    projected_utilization_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metrics.LambdaFunctionMemoryProjectedMetrics"
    ]
    """<p>An array of objects that describe the projected utilization metrics of the function recommendation option.</p>"""
    savings_opportunity: NotRequired[
        "aws_sdk_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    """<p>An object that describes the savings opportunity for the Lambda function recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.</p>"""
    savings_opportunity_after_discounts: NotRequired[
        "aws_sdk_compute_optimizer.types.lambda_savings_opportunity_after_discounts.LambdaSavingsOpportunityAfterDiscounts"
    ]
    """<p> An object that describes the savings opportunity for the Lambda recommendation option which includes Saving Plans discounts. Savings opportunity includes the estimated monthly savings and percentage. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryRecommendationOption) -> dict:
    out: dict = {}
    out["rank"] = value.get("rank", 0)
    out["memorySize"] = value.get("memory_size", 0)
    if "projected_utilization_metrics" in value:
        import aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metrics

        out["projectedUtilizationMetrics"] = (
            aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metrics.serialize_aws_json_1_0(
                value["projected_utilization_metrics"]
            )
        )
    if "savings_opportunity" in value:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import aws_sdk_compute_optimizer.types.lambda_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            aws_sdk_compute_optimizer.types.lambda_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionMemoryRecommendationOption:
    out: LambdaFunctionMemoryRecommendationOption = {}  # type: ignore[typeddict-item]
    if "rank" in data:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if "memorySize" in data:
        out["memory_size"] = data["memorySize"]
    else:
        out["memory_size"] = 0
    if "projectedUtilizationMetrics" in data:
        import aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metrics

        out["projected_utilization_metrics"] = (
            aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metrics.deserialize_aws_json_1_0(
                data["projectedUtilizationMetrics"]
            )
        )
    if "savingsOpportunity" in data:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if "savingsOpportunityAfterDiscounts" in data:
        import aws_sdk_compute_optimizer.types.lambda_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            aws_sdk_compute_optimizer.types.lambda_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    return out
