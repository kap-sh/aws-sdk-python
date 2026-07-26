"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisJobStatus``."""

from typing import Literal, TypeAlias, cast

MediaAnalysisJobStatus: TypeAlias = Literal[
    "CREATED",
    "QUEUED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MediaAnalysisJobStatus:
    return cast(MediaAnalysisJobStatus, data)
