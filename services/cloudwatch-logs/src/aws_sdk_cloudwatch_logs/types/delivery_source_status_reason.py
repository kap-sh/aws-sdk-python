"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceStatusReason``."""

from typing import Literal, TypeAlias, cast

DeliverySourceStatusReason: TypeAlias = Literal["RESOURCE_DELETED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySourceStatusReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliverySourceStatusReason:
    return cast(DeliverySourceStatusReason, data)
