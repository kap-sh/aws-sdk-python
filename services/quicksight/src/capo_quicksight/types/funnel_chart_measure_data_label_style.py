"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartMeasureDataLabelStyle``."""

from typing import Literal, TypeAlias, cast

FunnelChartMeasureDataLabelStyle: TypeAlias = Literal[
    "VALUE_ONLY",
    "PERCENTAGE_BY_FIRST_STAGE",
    "PERCENTAGE_BY_PREVIOUS_STAGE",
    "VALUE_AND_PERCENTAGE_BY_FIRST_STAGE",
    "VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartMeasureDataLabelStyle) -> str:
    return value


def deserialize_json(data: str) -> FunnelChartMeasureDataLabelStyle:
    return cast(FunnelChartMeasureDataLabelStyle, data)
