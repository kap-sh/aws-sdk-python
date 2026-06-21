"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryDeletionStatus``."""

from typing import Literal, TypeAlias, cast

InventoryDeletionStatus: TypeAlias = Literal[
    "InProgress",
    "Complete",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryDeletionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventoryDeletionStatus:
    return cast(InventoryDeletionStatus, data)
