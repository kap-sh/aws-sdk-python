"""Generated from Smithy shape ``com.amazonaws.qbusiness#PermissionConditionOperator``."""

from typing import Literal, TypeAlias, cast

PermissionConditionOperator: TypeAlias = Literal["StringEquals",]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionConditionOperator) -> str:
    return value


def deserialize_json(data: str) -> PermissionConditionOperator:
    return cast(PermissionConditionOperator, data)
