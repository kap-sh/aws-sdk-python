"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_allocation_tag_status_entry

CostAllocationTagStatusList: TypeAlias = list[
    "capo_cost_explorer.types.cost_allocation_tag_status_entry.CostAllocationTagStatusEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagStatusList) -> list:
    import capo_cost_explorer.types.cost_allocation_tag_status_entry

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.cost_allocation_tag_status_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostAllocationTagStatusList:
    import capo_cost_explorer.types.cost_allocation_tag_status_entry

    out: CostAllocationTagStatusList = []
    for item in data:
        out.append(
            capo_cost_explorer.types.cost_allocation_tag_status_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
