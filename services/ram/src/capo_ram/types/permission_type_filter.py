"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTypeFilter``."""

from typing import Literal, TypeAlias, cast

PermissionTypeFilter: TypeAlias = Literal[
    "ALL",
    "AWS_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTypeFilter) -> str:
    return value


def deserialize_json(data: str) -> PermissionTypeFilter:
    return cast(PermissionTypeFilter, data)
