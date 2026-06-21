"""Generated from Smithy shape ``com.amazonaws.quicksight#ForecastComputationSeasonality``."""

from typing import Literal, TypeAlias, cast

ForecastComputationSeasonality: TypeAlias = Literal[
    "AUTOMATIC",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ForecastComputationSeasonality) -> str:
    return value


def deserialize_json(data: str) -> ForecastComputationSeasonality:
    return cast(ForecastComputationSeasonality, data)
