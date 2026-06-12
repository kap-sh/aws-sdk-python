"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_group

InventoryGroupList: TypeAlias = list["aws_sdk_ssm.types.inventory_group.InventoryGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryGroupList) -> list:
    import aws_sdk_ssm.types.inventory_group

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.inventory_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryGroupList:
    import aws_sdk_ssm.types.inventory_group

    out: InventoryGroupList = []
    for item in data:
        out.append(aws_sdk_ssm.types.inventory_group.deserialize_aws_json_1_1(item))
    return out
