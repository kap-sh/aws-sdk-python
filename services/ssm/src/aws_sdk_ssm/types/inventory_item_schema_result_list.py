"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemSchemaResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_schema

InventoryItemSchemaResultList: TypeAlias = list[
    "aws_sdk_ssm.types.inventory_item_schema.InventoryItemSchema"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemSchemaResultList) -> list:
    import aws_sdk_ssm.types.inventory_item_schema

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.inventory_item_schema.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryItemSchemaResultList:
    import aws_sdk_ssm.types.inventory_item_schema

    out: InventoryItemSchemaResultList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.inventory_item_schema.deserialize_aws_json_1_1(item)
        )
    return out
