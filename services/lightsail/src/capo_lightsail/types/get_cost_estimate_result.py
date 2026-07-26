"""Generated from Smithy shape ``com.amazonaws.lightsail#GetCostEstimateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resources_budget_estimate


class GetCostEstimateResult(TypedDict, closed=True):
    resources_budget_estimate: NotRequired[
        "capo_lightsail.types.resources_budget_estimate.ResourcesBudgetEstimate"
    ]
    """<p>Returns the estimate's forecasted cost or usage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostEstimateResult) -> dict:
    out: dict = {}
    if "resources_budget_estimate" in value:
        import capo_lightsail.types.resources_budget_estimate

        out["resourcesBudgetEstimate"] = (
            capo_lightsail.types.resources_budget_estimate.serialize_aws_json_1_1(
                value["resources_budget_estimate"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostEstimateResult:
    out: GetCostEstimateResult = {}  # type: ignore[typeddict-item]
    if "resourcesBudgetEstimate" in data:
        import capo_lightsail.types.resources_budget_estimate

        out["resources_budget_estimate"] = (
            capo_lightsail.types.resources_budget_estimate.deserialize_aws_json_1_1(
                data["resourcesBudgetEstimate"]
            )
        )
    return out
