"""Generated from Smithy shape ``com.amazonaws.lakeformation#PermissionType``."""

from typing import Literal, TypeAlias, cast

PermissionType: TypeAlias = Literal[
    "COLUMN_PERMISSION",
    "CELL_FILTER_PERMISSION",
    "NESTED_PERMISSION",
    "NESTED_CELL_PERMISSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionType) -> str:
    return value


def deserialize_json(data: str) -> PermissionType:
    return cast(PermissionType, data)
