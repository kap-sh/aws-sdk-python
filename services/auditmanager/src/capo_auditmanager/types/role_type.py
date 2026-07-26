"""Generated from Smithy shape ``com.amazonaws.auditmanager#RoleType``."""

from typing import Literal, TypeAlias, cast

RoleType: TypeAlias = Literal[
    "PROCESS_OWNER",
    "RESOURCE_OWNER",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoleType) -> str:
    return value


def deserialize_json(data: str) -> RoleType:
    return cast(RoleType, data)
