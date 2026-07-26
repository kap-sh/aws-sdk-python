"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansUtilizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.savings_plans_utilization_aggregates
    import capo_cost_explorer.types.savings_plans_utilizations_by_time


class GetSavingsPlansUtilizationResponse(TypedDict, closed=True):
    savings_plans_utilizations_by_time: NotRequired[
        "capo_cost_explorer.types.savings_plans_utilizations_by_time.SavingsPlansUtilizationsByTime"
    ]
    """<p>The amount of cost/commitment that you used your Savings Plans. You can use it to specify date ranges.</p>"""
    total: "capo_cost_explorer.types.savings_plans_utilization_aggregates.SavingsPlansUtilizationAggregates"
    """<p>The total amount of cost/commitment that you used your Savings Plans, regardless of date ranges.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSavingsPlansUtilizationResponse) -> dict:
    out: dict = {}
    if "savings_plans_utilizations_by_time" in value:
        import capo_cost_explorer.types.savings_plans_utilizations_by_time

        out["SavingsPlansUtilizationsByTime"] = (
            capo_cost_explorer.types.savings_plans_utilizations_by_time.serialize_aws_json_1_1(
                value["savings_plans_utilizations_by_time"]
            )
        )
    import capo_cost_explorer.types.savings_plans_utilization_aggregates

    out["Total"] = (
        capo_cost_explorer.types.savings_plans_utilization_aggregates.serialize_aws_json_1_1(
            value["total"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSavingsPlansUtilizationResponse:
    out: GetSavingsPlansUtilizationResponse = {}  # type: ignore[typeddict-item]
    if "SavingsPlansUtilizationsByTime" in data:
        import capo_cost_explorer.types.savings_plans_utilizations_by_time

        out["savings_plans_utilizations_by_time"] = (
            capo_cost_explorer.types.savings_plans_utilizations_by_time.deserialize_aws_json_1_1(
                data["SavingsPlansUtilizationsByTime"]
            )
        )
    if "Total" in data:
        import capo_cost_explorer.types.savings_plans_utilization_aggregates

        out["total"] = (
            capo_cost_explorer.types.savings_plans_utilization_aggregates.deserialize_aws_json_1_1(
                data["Total"]
            )
        )
    else:
        raise DeserializationError("GetSavingsPlansUtilizationResponse.total required")
    return out
