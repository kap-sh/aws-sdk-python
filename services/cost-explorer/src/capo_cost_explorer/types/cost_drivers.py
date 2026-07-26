"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostDrivers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_driver

CostDrivers: TypeAlias = list["capo_cost_explorer.types.cost_driver.CostDriver"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostDrivers) -> list:
    import capo_cost_explorer.types.cost_driver

    out: list = []
    for item in value:
        out.append(capo_cost_explorer.types.cost_driver.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CostDrivers:
    import capo_cost_explorer.types.cost_driver

    out: CostDrivers = []
    for item in data:
        out.append(capo_cost_explorer.types.cost_driver.deserialize_aws_json_1_1(item))
    return out
