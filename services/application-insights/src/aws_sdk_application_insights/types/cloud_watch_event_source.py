"""Generated from Smithy shape ``com.amazonaws.applicationinsights#CloudWatchEventSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

CloudWatchEventSource: TypeAlias = Literal[
    "EC2",
    "CODE_DEPLOY",
    "HEALTH",
    "RDS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "CODE_DEPLOY",
        "HEALTH",
        "RDS",
    )
)


def serialize_aws_json_1_1(value: CloudWatchEventSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudWatchEventSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloudWatchEventSource value: {data!r}")
    return cast(CloudWatchEventSource, data)
