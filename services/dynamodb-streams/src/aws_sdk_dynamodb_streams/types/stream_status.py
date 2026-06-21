"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#StreamStatus``."""

from typing import Literal, TypeAlias, cast

StreamStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StreamStatus:
    return cast(StreamStatus, data)
