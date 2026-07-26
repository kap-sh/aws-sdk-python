"""Generated from Smithy shape ``com.amazonaws.forecast#ForecastDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.name

ForecastDimensions: TypeAlias = list["capo_forecast.types.name.Name"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForecastDimensions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ForecastDimensions:
    return list(data)
