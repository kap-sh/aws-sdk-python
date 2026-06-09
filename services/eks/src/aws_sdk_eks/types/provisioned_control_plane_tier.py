"""Generated from Smithy shape ``com.amazonaws.eks#ProvisionedControlPlaneTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

ProvisionedControlPlaneTier: TypeAlias = Literal[
    "standard",
    "tier-xl",
    "tier-2xl",
    "tier-4xl",
    "tier-8xl",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "tier-xl",
        "tier-2xl",
        "tier-4xl",
        "tier-8xl",
    )
)


def serialize_json(value: ProvisionedControlPlaneTier) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedControlPlaneTier:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProvisionedControlPlaneTier value: {data!r}"
        )
    return cast(ProvisionedControlPlaneTier, data)
