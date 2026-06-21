"""Generated from Smithy shape ``com.amazonaws.codebuild#LogsConfigStatusType``."""

from typing import Literal, TypeAlias, cast

LogsConfigStatusType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogsConfigStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogsConfigStatusType:
    return cast(LogsConfigStatusType, data)
