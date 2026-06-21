"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroupMembershipStatus``."""

from typing import Literal, TypeAlias, cast

PermissionGroupMembershipStatus: TypeAlias = Literal[
    "ADDITION_IN_PROGRESS",
    "ADDITION_SUCCESS",
    "REMOVAL_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionGroupMembershipStatus) -> str:
    return value


def deserialize_json(data: str) -> PermissionGroupMembershipStatus:
    return cast(PermissionGroupMembershipStatus, data)
