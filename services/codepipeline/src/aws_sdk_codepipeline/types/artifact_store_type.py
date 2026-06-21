"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactStoreType``."""

from typing import Literal, TypeAlias, cast

ArtifactStoreType: TypeAlias = Literal["S3",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactStoreType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactStoreType:
    return cast(ArtifactStoreType, data)
