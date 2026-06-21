"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactLocationType``."""

from typing import Literal, TypeAlias, cast

ArtifactLocationType: TypeAlias = Literal["S3",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactLocationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactLocationType:
    return cast(ArtifactLocationType, data)
