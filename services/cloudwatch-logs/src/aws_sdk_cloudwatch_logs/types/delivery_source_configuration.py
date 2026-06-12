"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_key
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_value

DeliverySourceConfiguration: TypeAlias = dict[
    "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_key.DeliverySourceConfigurationKey",
    "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_value.DeliverySourceConfigurationValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DeliverySourceConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliverySourceConfiguration:
    out: DeliverySourceConfiguration = {}
    for key, value in data.items():
        out[key] = value
    return out
