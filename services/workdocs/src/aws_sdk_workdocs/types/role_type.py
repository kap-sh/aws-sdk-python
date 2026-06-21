"""Generated from Smithy shape ``com.amazonaws.workdocs#RoleType``."""

from typing import Literal, TypeAlias, cast

RoleType: TypeAlias = Literal[
    "VIEWER",
    "CONTRIBUTOR",
    "OWNER",
    "COOWNER",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoleType) -> str:
    return value


def deserialize_json(data: str) -> RoleType:
    return cast(RoleType, data)
