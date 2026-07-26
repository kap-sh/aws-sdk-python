"""Generated from Smithy shape ``com.amazonaws.qbusiness#PermissionConditionValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.permission_condition_value

PermissionConditionValues: TypeAlias = list[
    "capo_qbusiness.types.permission_condition_value.PermissionConditionValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionConditionValues) -> list:
    return list(value)


def deserialize_json(data: list) -> PermissionConditionValues:
    return list(data)
