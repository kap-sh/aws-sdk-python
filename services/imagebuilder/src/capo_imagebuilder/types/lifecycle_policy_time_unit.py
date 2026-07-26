"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyTimeUnit``."""

from typing import Literal, TypeAlias, cast

LifecyclePolicyTimeUnit: TypeAlias = Literal[
    "DAYS",
    "WEEKS",
    "MONTHS",
    "YEARS",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyTimeUnit) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyTimeUnit:
    return cast(LifecyclePolicyTimeUnit, data)
