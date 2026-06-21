"""Generated from Smithy shape ``com.amazonaws.rekognition#VideoJobStatus``."""

from typing import Literal, TypeAlias, cast

VideoJobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VideoJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VideoJobStatus:
    return cast(VideoJobStatus, data)
