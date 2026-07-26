"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWeightConstraintType``."""

from typing import Literal, TypeAlias, cast

RouteWeightConstraintType: TypeAlias = Literal[
    "Current",
    "Gross",
    "Unknown",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteWeightConstraintType) -> str:
    return value


def deserialize_json(data: str) -> RouteWeightConstraintType:
    return cast(RouteWeightConstraintType, data)
