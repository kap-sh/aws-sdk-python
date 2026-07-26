"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCategorySpecificSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.trusted_advisor_cost_optimizing_summary


class TrustedAdvisorCategorySpecificSummary(TypedDict, closed=True):
    cost_optimizing: NotRequired[
        "capo_support.types.trusted_advisor_cost_optimizing_summary.TrustedAdvisorCostOptimizingSummary"
    ]
    """<p>The summary information about cost savings for a Trusted Advisor check that is in the Cost Optimizing category.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCategorySpecificSummary) -> dict:
    out: dict = {}
    if "cost_optimizing" in value:
        import capo_support.types.trusted_advisor_cost_optimizing_summary

        out["costOptimizing"] = (
            capo_support.types.trusted_advisor_cost_optimizing_summary.serialize_aws_json_1_1(
                value["cost_optimizing"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorCategorySpecificSummary:
    out: TrustedAdvisorCategorySpecificSummary = {}  # type: ignore[typeddict-item]
    if "costOptimizing" in data:
        import capo_support.types.trusted_advisor_cost_optimizing_summary

        out["cost_optimizing"] = (
            capo_support.types.trusted_advisor_cost_optimizing_summary.deserialize_aws_json_1_1(
                data["costOptimizing"]
            )
        )
    return out
