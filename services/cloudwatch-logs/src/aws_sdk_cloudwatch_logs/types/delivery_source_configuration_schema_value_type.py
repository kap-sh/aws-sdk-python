"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceConfigurationSchemaValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

DeliverySourceConfigurationSchemaValueType: TypeAlias = Literal[
    "string",
    "boolean",
    "int",
    "double",
    "long",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "string",
        "boolean",
        "int",
        "double",
        "long",
    )
)


def serialize_aws_json_1_1(value: DeliverySourceConfigurationSchemaValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliverySourceConfigurationSchemaValueType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeliverySourceConfigurationSchemaValueType value: {data!r}"
        )
    return cast(DeliverySourceConfigurationSchemaValueType, data)
