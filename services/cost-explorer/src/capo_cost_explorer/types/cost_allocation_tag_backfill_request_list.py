"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagBackfillRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_allocation_tag_backfill_request

CostAllocationTagBackfillRequestList: TypeAlias = list[
    "capo_cost_explorer.types.cost_allocation_tag_backfill_request.CostAllocationTagBackfillRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagBackfillRequestList) -> list:
    import capo_cost_explorer.types.cost_allocation_tag_backfill_request

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.cost_allocation_tag_backfill_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostAllocationTagBackfillRequestList:
    import capo_cost_explorer.types.cost_allocation_tag_backfill_request

    out: CostAllocationTagBackfillRequestList = []
    for item in data:
        out.append(
            capo_cost_explorer.types.cost_allocation_tag_backfill_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
