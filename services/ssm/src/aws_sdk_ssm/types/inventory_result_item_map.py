"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryResultItemMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_result_item
    import aws_sdk_ssm.types.inventory_result_item_key

InventoryResultItemMap: TypeAlias = dict[
    "aws_sdk_ssm.types.inventory_result_item_key.InventoryResultItemKey",
    "aws_sdk_ssm.types.inventory_result_item.InventoryResultItem",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: InventoryResultItemMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.inventory_result_item

        out[key] = aws_sdk_ssm.types.inventory_result_item.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryResultItemMap:
    out: InventoryResultItemMap = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.inventory_result_item

        out[key] = aws_sdk_ssm.types.inventory_result_item.deserialize_aws_json_1_1(
            value
        )
    return out
