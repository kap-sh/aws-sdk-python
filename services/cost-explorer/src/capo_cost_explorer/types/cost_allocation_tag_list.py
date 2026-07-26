"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_allocation_tag

CostAllocationTagList: TypeAlias = list[
    "capo_cost_explorer.types.cost_allocation_tag.CostAllocationTag"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagList) -> list:
    import capo_cost_explorer.types.cost_allocation_tag

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.cost_allocation_tag.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostAllocationTagList:
    import capo_cost_explorer.types.cost_allocation_tag

    out: CostAllocationTagList = []
    for item in data:
        out.append(
            capo_cost_explorer.types.cost_allocation_tag.deserialize_aws_json_1_1(item)
        )
    return out
