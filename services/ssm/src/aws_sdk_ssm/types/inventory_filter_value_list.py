"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_filter_value

InventoryFilterValueList: TypeAlias = list[
    "aws_sdk_ssm.types.inventory_filter_value.InventoryFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InventoryFilterValueList:
    return list(data)
