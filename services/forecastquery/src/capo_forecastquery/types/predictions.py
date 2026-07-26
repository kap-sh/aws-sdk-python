"""Generated from Smithy shape ``com.amazonaws.forecastquery#Predictions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecastquery.types.statistic
    import capo_forecastquery.types.time_series

Predictions: TypeAlias = dict[
    "capo_forecastquery.types.statistic.Statistic",
    "capo_forecastquery.types.time_series.TimeSeries",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Predictions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_forecastquery.types.time_series

        out[key] = capo_forecastquery.types.time_series.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> Predictions:
    out: Predictions = {}
    for key, value in data.items():
        import capo_forecastquery.types.time_series

        out[key] = capo_forecastquery.types.time_series.deserialize_aws_json_1_1(value)
    return out
