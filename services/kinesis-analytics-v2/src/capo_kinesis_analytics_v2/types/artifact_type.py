"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ArtifactType``."""

from typing import Literal, TypeAlias, cast

ArtifactType: TypeAlias = Literal[
    "UDF",
    "DEPENDENCY_JAR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactType:
    return cast(ArtifactType, data)
