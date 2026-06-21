"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryQueryOperatorType``."""

from typing import Literal, TypeAlias, cast

InventoryQueryOperatorType: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "BeginWith",
    "LessThan",
    "GreaterThan",
    "Exists",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryQueryOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventoryQueryOperatorType:
    return cast(InventoryQueryOperatorType, data)
