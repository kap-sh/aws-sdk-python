"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorStatus``."""

from typing import Literal, TypeAlias, cast

StreamProcessorStatus: TypeAlias = Literal[
    "STOPPED",
    "STARTING",
    "RUNNING",
    "FAILED",
    "STOPPING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamProcessorStatus:
    return cast(StreamProcessorStatus, data)
