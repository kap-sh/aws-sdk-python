"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

DeliverySourceStatusReason: TypeAlias = Literal["RESOURCE_DELETED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RESOURCE_DELETED",))


def serialize_aws_json_1_1(value: DeliverySourceStatusReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliverySourceStatusReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeliverySourceStatusReason value: {data!r}"
        )
    return cast(DeliverySourceStatusReason, data)
