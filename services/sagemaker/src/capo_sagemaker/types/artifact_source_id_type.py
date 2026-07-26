"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactSourceIdType``."""

from typing import Literal, TypeAlias, cast

ArtifactSourceIdType: TypeAlias = Literal[
    "MD5Hash",
    "S3ETag",
    "S3Version",
    "Custom",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactSourceIdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactSourceIdType:
    return cast(ArtifactSourceIdType, data)
