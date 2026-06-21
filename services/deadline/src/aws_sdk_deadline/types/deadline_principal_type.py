"""Generated from Smithy shape ``com.amazonaws.deadline#DeadlinePrincipalType``."""

from typing import Literal, TypeAlias, cast

DeadlinePrincipalType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeadlinePrincipalType) -> str:
    return value


def deserialize_json(data: str) -> DeadlinePrincipalType:
    return cast(DeadlinePrincipalType, data)
