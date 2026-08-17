"""Generated from Smithy shape ``com.amazonaws.ecr#ArtifactTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.artifact_type

ArtifactTypeList: TypeAlias = list["capo_ecr.types.artifact_type.ArtifactType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ArtifactTypeList:
    return [item for item in data if item is not None]
