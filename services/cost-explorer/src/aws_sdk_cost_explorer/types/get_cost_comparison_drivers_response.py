"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostComparisonDriversResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_comparison_drivers
    import aws_sdk_cost_explorer.types.next_page_token


class GetCostComparisonDriversResponse(TypedDict, closed=True):
    cost_comparison_drivers: NotRequired[
        "aws_sdk_cost_explorer.types.cost_comparison_drivers.CostComparisonDrivers"
    ]
    """<p>An array of comparison results showing factors that drive significant cost differences between <code>BaselineTimePeriod</code> and <code>ComparisonTimePeriod</code>.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of paginated results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostComparisonDriversResponse) -> dict:
    out: dict = {}
    if "cost_comparison_drivers" in value:
        import aws_sdk_cost_explorer.types.cost_comparison_drivers

        out["CostComparisonDrivers"] = (
            aws_sdk_cost_explorer.types.cost_comparison_drivers.serialize_aws_json_1_1(
                value["cost_comparison_drivers"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostComparisonDriversResponse:
    out: GetCostComparisonDriversResponse = {}  # type: ignore[typeddict-item]
    if "CostComparisonDrivers" in data:
        import aws_sdk_cost_explorer.types.cost_comparison_drivers

        out["cost_comparison_drivers"] = (
            aws_sdk_cost_explorer.types.cost_comparison_drivers.deserialize_aws_json_1_1(
                data["CostComparisonDrivers"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
