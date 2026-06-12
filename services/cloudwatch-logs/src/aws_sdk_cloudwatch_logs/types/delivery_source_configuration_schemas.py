"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceConfigurationSchemas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema

DeliverySourceConfigurationSchemas: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema.DeliverySourceConfigurationSchema"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySourceConfigurationSchemas) -> list:
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeliverySourceConfigurationSchemas:
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema

    out: DeliverySourceConfigurationSchemas = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema.deserialize_aws_json_1_1(
                item
            )
        )
    return out
