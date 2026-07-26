"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactSourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.artifact_source_type

ArtifactSourceTypes: TypeAlias = list[
    "capo_sagemaker.types.artifact_source_type.ArtifactSourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactSourceTypes) -> list:
    import capo_sagemaker.types.artifact_source_type

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.artifact_source_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ArtifactSourceTypes:
    import capo_sagemaker.types.artifact_source_type

    out: ArtifactSourceTypes = []
    for item in data:
        out.append(
            capo_sagemaker.types.artifact_source_type.deserialize_aws_json_1_1(item)
        )
    return out
