"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemSchemaResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_schema

InventoryItemSchemaResultList: TypeAlias = list[
    "capo_ssm.types.inventory_item_schema.InventoryItemSchema"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemSchemaResultList) -> list:
    import capo_ssm.types.inventory_item_schema

    out: list = []
    for item in value:
        out.append(capo_ssm.types.inventory_item_schema.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryItemSchemaResultList:
    import capo_ssm.types.inventory_item_schema

    out: InventoryItemSchemaResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.inventory_item_schema.deserialize_aws_json_1_1(item))
    return out
