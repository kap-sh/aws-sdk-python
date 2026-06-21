"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailFilterType``."""

from typing import Literal, TypeAlias, cast

LifecyclePolicyDetailFilterType: TypeAlias = Literal[
    "AGE",
    "COUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailFilterType) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyDetailFilterType:
    return cast(LifecyclePolicyDetailFilterType, data)
