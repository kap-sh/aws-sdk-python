"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchResourceStatusType``."""

from typing import Literal, TypeAlias, cast

OpenSearchResourceStatusType: TypeAlias = Literal[
    "ACTIVE",
    "NOT_FOUND",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchResourceStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenSearchResourceStatusType:
    return cast(OpenSearchResourceStatusType, data)
