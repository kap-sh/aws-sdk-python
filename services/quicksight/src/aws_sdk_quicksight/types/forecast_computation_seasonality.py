"""Generated from Smithy shape ``com.amazonaws.quicksight#ForecastComputationSeasonality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ForecastComputationSeasonality: TypeAlias = Literal[
    "AUTOMATIC",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "CUSTOM",
    )
)


def serialize_json(value: ForecastComputationSeasonality) -> str:
    return value


def deserialize_json(data: str) -> ForecastComputationSeasonality:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ForecastComputationSeasonality value: {data!r}"
        )
    return cast(ForecastComputationSeasonality, data)
