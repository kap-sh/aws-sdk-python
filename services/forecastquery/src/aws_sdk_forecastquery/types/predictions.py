"""Generated from Smithy shape ``com.amazonaws.forecastquery#Predictions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecastquery.types.statistic
    import aws_sdk_forecastquery.types.time_series

Predictions: TypeAlias = dict[
    "aws_sdk_forecastquery.types.statistic.Statistic",
    "aws_sdk_forecastquery.types.time_series.TimeSeries",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Predictions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_forecastquery.types.time_series

        out[key] = aws_sdk_forecastquery.types.time_series.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> Predictions:
    out: Predictions = {}
    for key, value in data.items():
        import aws_sdk_forecastquery.types.time_series

        out[key] = aws_sdk_forecastquery.types.time_series.deserialize_aws_json_1_1(
            value
        )
    return out
