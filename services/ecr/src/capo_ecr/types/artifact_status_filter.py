"""Generated from Smithy shape ``com.amazonaws.ecr#ArtifactStatusFilter``."""

from typing import Literal, TypeAlias, cast

ArtifactStatusFilter: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ACTIVATING",
    "ANY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactStatusFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactStatusFilter:
    return cast(ArtifactStatusFilter, data)
