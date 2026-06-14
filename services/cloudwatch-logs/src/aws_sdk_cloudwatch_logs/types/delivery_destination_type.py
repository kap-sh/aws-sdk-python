"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliveryDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

DeliveryDestinationType: TypeAlias = Literal[
    "S3",
    "CWL",
    "FH",
    "XRAY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "CWL",
        "FH",
        "XRAY",
    )
)


def serialize_aws_json_1_1(value: DeliveryDestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryDestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryDestinationType value: {data!r}")
    return cast(DeliveryDestinationType, data)
