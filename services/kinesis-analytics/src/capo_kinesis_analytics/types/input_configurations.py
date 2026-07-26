"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.input_configuration

InputConfigurations: TypeAlias = list[
    "capo_kinesis_analytics.types.input_configuration.InputConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputConfigurations) -> list:
    import capo_kinesis_analytics.types.input_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics.types.input_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InputConfigurations:
    import capo_kinesis_analytics.types.input_configuration

    out: InputConfigurations = []
    for item in data:
        out.append(
            capo_kinesis_analytics.types.input_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
