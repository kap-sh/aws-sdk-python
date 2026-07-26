"""Generated from Smithy shape ``com.amazonaws.ecr#ArtifactStatus``."""

from typing import Literal, TypeAlias, cast

ArtifactStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ACTIVATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactStatus:
    return cast(ArtifactStatus, data)
