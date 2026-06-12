"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWeightConstraintType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteWeightConstraintType: TypeAlias = Literal[
    "Current",
    "Gross",
    "Unknown",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Current",
        "Gross",
        "Unknown",
    )
)


def serialize_json(value: RouteWeightConstraintType) -> str:
    return value


def deserialize_json(data: str) -> RouteWeightConstraintType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteWeightConstraintType value: {data!r}")
    return cast(RouteWeightConstraintType, data)
