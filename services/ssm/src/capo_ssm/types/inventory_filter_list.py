"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.inventory_filter

InventoryFilterList: TypeAlias = list["capo_ssm.types.inventory_filter.InventoryFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryFilterList) -> list:
    import capo_ssm.types.inventory_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.inventory_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryFilterList:
    import capo_ssm.types.inventory_filter

    out: InventoryFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.inventory_filter.deserialize_aws_json_1_1(item))
    return out
