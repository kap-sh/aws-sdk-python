"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceConfigurationSupportedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_source_configuration_schema_field

DeliverySourceConfigurationSupportedValues: TypeAlias = list[
    "capo_cloudwatch_logs.types.delivery_source_configuration_schema_field.DeliverySourceConfigurationSchemaField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySourceConfigurationSupportedValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeliverySourceConfigurationSupportedValues:
    return [item for item in data if item is not None]
