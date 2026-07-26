"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesTransformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.time_series_transformation

TimeSeriesTransformations: TypeAlias = list[
    "capo_forecast.types.time_series_transformation.TimeSeriesTransformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesTransformations) -> list:
    import capo_forecast.types.time_series_transformation

    out: list = []
    for item in value:
        out.append(
            capo_forecast.types.time_series_transformation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TimeSeriesTransformations:
    import capo_forecast.types.time_series_transformation

    out: TimeSeriesTransformations = []
    for item in data:
        out.append(
            capo_forecast.types.time_series_transformation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
