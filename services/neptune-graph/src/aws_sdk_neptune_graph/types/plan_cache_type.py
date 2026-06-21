"""Generated from Smithy shape ``com.amazonaws.neptunegraph#PlanCacheType``."""

from typing import Literal, TypeAlias, cast

PlanCacheType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: PlanCacheType) -> str:
    return value


def deserialize_json(data: str) -> PlanCacheType:
    return cast(PlanCacheType, data)
