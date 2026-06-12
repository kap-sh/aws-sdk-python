"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineOptimizationObjective``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

IsolineOptimizationObjective: TypeAlias = Literal[
    "AccurateCalculation",
    "BalancedCalculation",
    "FastCalculation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccurateCalculation",
        "BalancedCalculation",
        "FastCalculation",
    )
)


def serialize_json(value: IsolineOptimizationObjective) -> str:
    return value


def deserialize_json(data: str) -> IsolineOptimizationObjective:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IsolineOptimizationObjective value: {data!r}"
        )
    return cast(IsolineOptimizationObjective, data)
