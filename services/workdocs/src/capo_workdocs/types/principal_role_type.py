"""Generated from Smithy shape ``com.amazonaws.workdocs#PrincipalRoleType``."""

from typing import Literal, TypeAlias, cast

PrincipalRoleType: TypeAlias = Literal[
    "VIEWER",
    "CONTRIBUTOR",
    "OWNER",
    "COOWNER",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalRoleType) -> str:
    return value


def deserialize_json(data: str) -> PrincipalRoleType:
    return cast(PrincipalRoleType, data)
