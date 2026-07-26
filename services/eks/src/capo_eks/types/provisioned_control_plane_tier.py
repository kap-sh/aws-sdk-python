"""Generated from Smithy shape ``com.amazonaws.eks#ProvisionedControlPlaneTier``."""

from typing import Literal, TypeAlias, cast

ProvisionedControlPlaneTier: TypeAlias = Literal[
    "standard",
    "tier-xl",
    "tier-2xl",
    "tier-4xl",
    "tier-8xl",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedControlPlaneTier) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedControlPlaneTier:
    return cast(ProvisionedControlPlaneTier, data)
