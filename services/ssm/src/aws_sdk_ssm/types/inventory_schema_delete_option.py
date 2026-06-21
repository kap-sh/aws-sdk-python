"""Generated from Smithy shape ``com.amazonaws.ssm#InventorySchemaDeleteOption``."""

from typing import Literal, TypeAlias, cast

InventorySchemaDeleteOption: TypeAlias = Literal[
    "DisableSchema",
    "DeleteSchema",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventorySchemaDeleteOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventorySchemaDeleteOption:
    return cast(InventorySchemaDeleteOption, data)
