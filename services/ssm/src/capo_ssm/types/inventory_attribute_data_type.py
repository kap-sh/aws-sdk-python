"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryAttributeDataType``."""

from typing import Literal, TypeAlias, cast

InventoryAttributeDataType: TypeAlias = Literal[
    "string",
    "number",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryAttributeDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventoryAttributeDataType:
    return cast(InventoryAttributeDataType, data)
