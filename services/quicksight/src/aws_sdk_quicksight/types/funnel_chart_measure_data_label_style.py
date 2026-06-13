"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartMeasureDataLabelStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FunnelChartMeasureDataLabelStyle: TypeAlias = Literal[
    "VALUE_ONLY",
    "PERCENTAGE_BY_FIRST_STAGE",
    "PERCENTAGE_BY_PREVIOUS_STAGE",
    "VALUE_AND_PERCENTAGE_BY_FIRST_STAGE",
    "VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALUE_ONLY",
        "PERCENTAGE_BY_FIRST_STAGE",
        "PERCENTAGE_BY_PREVIOUS_STAGE",
        "VALUE_AND_PERCENTAGE_BY_FIRST_STAGE",
        "VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE",
    )
)


def serialize_json(value: FunnelChartMeasureDataLabelStyle) -> str:
    return value


def deserialize_json(data: str) -> FunnelChartMeasureDataLabelStyle:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FunnelChartMeasureDataLabelStyle value: {data!r}"
        )
    return cast(FunnelChartMeasureDataLabelStyle, data)
