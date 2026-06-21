"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsWorkStatus``."""

from typing import Literal, TypeAlias, cast

ReplacePermissionAssociationsWorkStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplacePermissionAssociationsWorkStatus) -> str:
    return value


def deserialize_json(data: str) -> ReplacePermissionAssociationsWorkStatus:
    return cast(ReplacePermissionAssociationsWorkStatus, data)
