"""Generated from Smithy shape ``com.amazonaws.glue#PermissionType``."""

from typing import Literal, TypeAlias, cast

PermissionType: TypeAlias = Literal[
    "COLUMN_PERMISSION",
    "CELL_FILTER_PERMISSION",
    "NESTED_PERMISSION",
    "NESTED_CELL_PERMISSION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PermissionType:
    return cast(PermissionType, data)
