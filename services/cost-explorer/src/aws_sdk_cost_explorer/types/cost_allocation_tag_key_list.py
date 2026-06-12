"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.tag_key

CostAllocationTagKeyList: TypeAlias = list["aws_sdk_cost_explorer.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CostAllocationTagKeyList:
    return list(data)
