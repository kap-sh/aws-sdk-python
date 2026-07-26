"""Generated from Smithy shape ``com.amazonaws.quicksight#ForecastConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.forecast_configuration

ForecastConfigurationList: TypeAlias = list[
    "capo_quicksight.types.forecast_configuration.ForecastConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ForecastConfigurationList) -> list:
    import capo_quicksight.types.forecast_configuration

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.forecast_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ForecastConfigurationList:
    import capo_quicksight.types.forecast_configuration

    out: ForecastConfigurationList = []
    for item in data:
        out.append(capo_quicksight.types.forecast_configuration.deserialize_json(item))
    return out
