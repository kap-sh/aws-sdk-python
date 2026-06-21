"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisJobFailureCode``."""

from typing import Literal, TypeAlias, cast

MediaAnalysisJobFailureCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "INVALID_S3_OBJECT",
    "INVALID_MANIFEST",
    "INVALID_OUTPUT_CONFIG",
    "INVALID_KMS_KEY",
    "ACCESS_DENIED",
    "RESOURCE_NOT_FOUND",
    "RESOURCE_NOT_READY",
    "THROTTLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisJobFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MediaAnalysisJobFailureCode:
    return cast(MediaAnalysisJobFailureCode, data)
