"""Generated from Smithy shape ``com.amazonaws.licensemanager#InventoryFilterCondition``."""

from typing import Literal, TypeAlias, cast

InventoryFilterCondition: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "BEGINS_WITH",
    "CONTAINS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryFilterCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventoryFilterCondition:
    return cast(InventoryFilterCondition, data)
