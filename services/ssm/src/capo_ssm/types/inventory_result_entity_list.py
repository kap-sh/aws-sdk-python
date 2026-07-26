"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryResultEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.inventory_result_entity

InventoryResultEntityList: TypeAlias = list[
    "capo_ssm.types.inventory_result_entity.InventoryResultEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryResultEntityList) -> list:
    import capo_ssm.types.inventory_result_entity

    out: list = []
    for item in value:
        out.append(capo_ssm.types.inventory_result_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryResultEntityList:
    import capo_ssm.types.inventory_result_entity

    out: InventoryResultEntityList = []
    for item in data:
        out.append(
            capo_ssm.types.inventory_result_entity.deserialize_aws_json_1_1(item)
        )
    return out
