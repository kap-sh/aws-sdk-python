"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsWorkStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ReplacePermissionAssociationsWorkStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: ReplacePermissionAssociationsWorkStatus) -> str:
    return value


def deserialize_json(data: str) -> ReplacePermissionAssociationsWorkStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReplacePermissionAssociationsWorkStatus value: {data!r}"
        )
    return cast(ReplacePermissionAssociationsWorkStatus, data)
