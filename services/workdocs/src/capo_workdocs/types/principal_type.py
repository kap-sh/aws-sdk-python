"""Generated from Smithy shape ``com.amazonaws.workdocs#PrincipalType``."""

from typing import Literal, TypeAlias, cast

PrincipalType: TypeAlias = Literal[
    "USER",
    "GROUP",
    "INVITE",
    "ANONYMOUS",
    "ORGANIZATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalType) -> str:
    return value


def deserialize_json(data: str) -> PrincipalType:
    return cast(PrincipalType, data)
