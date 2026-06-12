"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroupMembershipStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

PermissionGroupMembershipStatus: TypeAlias = Literal[
    "ADDITION_IN_PROGRESS",
    "ADDITION_SUCCESS",
    "REMOVAL_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADDITION_IN_PROGRESS",
        "ADDITION_SUCCESS",
        "REMOVAL_IN_PROGRESS",
    )
)


def serialize_json(value: PermissionGroupMembershipStatus) -> str:
    return value


def deserialize_json(data: str) -> PermissionGroupMembershipStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PermissionGroupMembershipStatus value: {data!r}"
        )
    return cast(PermissionGroupMembershipStatus, data)
