"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourcePricing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.estimated_discounts


class ResourcePricing(TypedDict, closed=True):
    estimated_cost_before_discounts: NotRequired["float"]
    """<p>The savings estimate using Amazon Web Services public pricing without incorporating any discounts.</p>"""
    estimated_net_unused_amortized_commitments: NotRequired["float"]
    """<p>The estimated net unused amortized commitment for the recommendation.</p>"""
    estimated_discounts: NotRequired[
        "aws_sdk_cost_optimization_hub.types.estimated_discounts.EstimatedDiscounts"
    ]
    """<p>The estimated discounts for a recommendation.</p>"""
    estimated_cost_after_discounts: NotRequired["float"]
    """<p>The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourcePricing) -> dict:
    out: dict = {}
    if "estimated_cost_before_discounts" in value:
        out["estimatedCostBeforeDiscounts"] = value["estimated_cost_before_discounts"]
    if "estimated_net_unused_amortized_commitments" in value:
        out["estimatedNetUnusedAmortizedCommitments"] = value[
            "estimated_net_unused_amortized_commitments"
        ]
    if "estimated_discounts" in value:
        import aws_sdk_cost_optimization_hub.types.estimated_discounts

        out["estimatedDiscounts"] = (
            aws_sdk_cost_optimization_hub.types.estimated_discounts.serialize_aws_json_1_0(
                value["estimated_discounts"]
            )
        )
    if "estimated_cost_after_discounts" in value:
        out["estimatedCostAfterDiscounts"] = value["estimated_cost_after_discounts"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourcePricing:
    out: ResourcePricing = {}  # type: ignore[typeddict-item]
    if "estimatedCostBeforeDiscounts" in data:
        out["estimated_cost_before_discounts"] = data["estimatedCostBeforeDiscounts"]
    if "estimatedNetUnusedAmortizedCommitments" in data:
        out["estimated_net_unused_amortized_commitments"] = data[
            "estimatedNetUnusedAmortizedCommitments"
        ]
    if "estimatedDiscounts" in data:
        import aws_sdk_cost_optimization_hub.types.estimated_discounts

        out["estimated_discounts"] = (
            aws_sdk_cost_optimization_hub.types.estimated_discounts.deserialize_aws_json_1_0(
                data["estimatedDiscounts"]
            )
        )
    if "estimatedCostAfterDiscounts" in data:
        out["estimated_cost_after_discounts"] = data["estimatedCostAfterDiscounts"]
    return out
