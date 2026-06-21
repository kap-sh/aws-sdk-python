"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortArtifactsBy``."""

from typing import Literal, TypeAlias, cast

SortArtifactsBy: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortArtifactsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortArtifactsBy:
    return cast(SortArtifactsBy, data)
