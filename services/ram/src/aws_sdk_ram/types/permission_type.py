"""Generated from Smithy shape ``com.amazonaws.ram#PermissionType``."""

from typing import Literal, TypeAlias, cast

PermissionType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionType) -> str:
    return value


def deserialize_json(data: str) -> PermissionType:
    return cast(PermissionType, data)
