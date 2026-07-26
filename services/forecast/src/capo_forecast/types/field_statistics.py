"""Generated from Smithy shape ``com.amazonaws.forecast#FieldStatistics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.statistics
    import capo_forecast.types.string

FieldStatistics: TypeAlias = dict[
    "capo_forecast.types.string.String", "capo_forecast.types.statistics.Statistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FieldStatistics) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_forecast.types.statistics

        out[key] = capo_forecast.types.statistics.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldStatistics:
    out: FieldStatistics = {}
    for key, value in data.items():
        import capo_forecast.types.statistics

        out[key] = capo_forecast.types.statistics.deserialize_aws_json_1_1(value)
    return out
