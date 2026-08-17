"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryResultItemMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.inventory_result_item
    import capo_ssm.types.inventory_result_item_key

InventoryResultItemMap: TypeAlias = dict[
    "capo_ssm.types.inventory_result_item_key.InventoryResultItemKey",
    "capo_ssm.types.inventory_result_item.InventoryResultItem",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: InventoryResultItemMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ssm.types.inventory_result_item

        out[key] = capo_ssm.types.inventory_result_item.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryResultItemMap:
    out: InventoryResultItemMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_ssm.types.inventory_result_item

        out[key] = capo_ssm.types.inventory_result_item.deserialize_aws_json_1_1(value)
    return out
