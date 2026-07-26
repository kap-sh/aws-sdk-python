"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyStatus``."""

from typing import Literal, TypeAlias, cast

LifecyclePolicyStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyStatus) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyStatus:
    return cast(LifecyclePolicyStatus, data)
