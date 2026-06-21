"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailActionType``."""

from typing import Literal, TypeAlias, cast

LifecyclePolicyDetailActionType: TypeAlias = Literal[
    "DELETE",
    "DEPRECATE",
    "DISABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailActionType) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyDetailActionType:
    return cast(LifecyclePolicyDetailActionType, data)
