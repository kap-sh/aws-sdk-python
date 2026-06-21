"""Generated from Smithy shape ``com.amazonaws.applicationinsights#CloudWatchEventSource``."""

from typing import Literal, TypeAlias, cast

CloudWatchEventSource: TypeAlias = Literal[
    "EC2",
    "CODE_DEPLOY",
    "HEALTH",
    "RDS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchEventSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudWatchEventSource:
    return cast(CloudWatchEventSource, data)
