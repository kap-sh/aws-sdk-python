"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EventSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

EventSource: TypeAlias = Literal[
    "CloudTrail",
    "Route53Resolver",
    "VPCFlow",
    "EKSAudit",
    "AWSWAF",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CloudTrail",
        "Route53Resolver",
        "VPCFlow",
        "EKSAudit",
        "AWSWAF",
    )
)


def serialize_aws_json_1_1(value: EventSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSource value: {data!r}")
    return cast(EventSource, data)
