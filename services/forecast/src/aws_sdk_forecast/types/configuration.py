"""Generated from Smithy shape ``com.amazonaws.forecast#Configuration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.values

Configuration: TypeAlias = dict[
    "aws_sdk_forecast.types.name.Name", "aws_sdk_forecast.types.values.Values"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Configuration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_forecast.types.values

        out[key] = aws_sdk_forecast.types.values.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> Configuration:
    out: Configuration = {}
    for key, value in data.items():
        import aws_sdk_forecast.types.values

        out[key] = aws_sdk_forecast.types.values.deserialize_aws_json_1_1(value)
    return out
