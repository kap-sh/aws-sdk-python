"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineOptimizationObjective``."""

from typing import Literal, TypeAlias, cast

IsolineOptimizationObjective: TypeAlias = Literal[
    "AccurateCalculation",
    "BalancedCalculation",
    "FastCalculation",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineOptimizationObjective) -> str:
    return value


def deserialize_json(data: str) -> IsolineOptimizationObjective:
    return cast(IsolineOptimizationObjective, data)
