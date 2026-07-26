"""Generated from Smithy shape ``com.amazonaws.qbusiness#PermissionConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.permission_condition

PermissionConditions: TypeAlias = list[
    "capo_qbusiness.types.permission_condition.PermissionCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionConditions) -> list:
    import capo_qbusiness.types.permission_condition

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.permission_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionConditions:
    import capo_qbusiness.types.permission_condition

    out: PermissionConditions = []
    for item in data:
        out.append(capo_qbusiness.types.permission_condition.deserialize_json(item))
    return out
