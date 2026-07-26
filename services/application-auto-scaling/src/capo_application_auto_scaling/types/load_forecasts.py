"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#LoadForecasts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.load_forecast

LoadForecasts: TypeAlias = list[
    "capo_application_auto_scaling.types.load_forecast.LoadForecast"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadForecasts) -> list:
    import capo_application_auto_scaling.types.load_forecast

    out: list = []
    for item in value:
        out.append(
            capo_application_auto_scaling.types.load_forecast.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LoadForecasts:
    import capo_application_auto_scaling.types.load_forecast

    out: LoadForecasts = []
    for item in data:
        out.append(
            capo_application_auto_scaling.types.load_forecast.deserialize_aws_json_1_1(
                item
            )
        )
    return out
