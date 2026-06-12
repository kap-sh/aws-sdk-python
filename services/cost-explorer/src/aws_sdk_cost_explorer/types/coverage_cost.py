"""Generated from Smithy shape ``com.amazonaws.costexplorer#CoverageCost``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.on_demand_cost


class CoverageCost(TypedDict):
    on_demand_cost: NotRequired[
        "aws_sdk_cost_explorer.types.on_demand_cost.OnDemandCost"
    ]
    """<p>How much an On-Demand Instance costs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CoverageCost) -> dict:
    out: dict = {}
    if "on_demand_cost" in value:
        out["OnDemandCost"] = value["on_demand_cost"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CoverageCost:
    out: CoverageCost = {}  # type: ignore[typeddict-item]
    if "OnDemandCost" in data:
        out["on_demand_cost"] = data["OnDemandCost"]
    return out
