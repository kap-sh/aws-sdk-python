"""Generated from Smithy shape ``com.amazonaws.eks#AccessScopeType``."""

from typing import Literal, TypeAlias, cast

AccessScopeType: TypeAlias = Literal[
    "cluster",
    "namespace",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessScopeType) -> str:
    return value


def deserialize_json(data: str) -> AccessScopeType:
    return cast(AccessScopeType, data)
