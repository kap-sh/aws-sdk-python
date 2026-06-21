"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceConfigurationSchemaValueType``."""

from typing import Literal, TypeAlias, cast

DeliverySourceConfigurationSchemaValueType: TypeAlias = Literal[
    "string",
    "boolean",
    "int",
    "double",
    "long",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySourceConfigurationSchemaValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliverySourceConfigurationSchemaValueType:
    return cast(DeliverySourceConfigurationSchemaValueType, data)
