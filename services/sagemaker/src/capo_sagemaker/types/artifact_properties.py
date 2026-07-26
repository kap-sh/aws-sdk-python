"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.artifact_property_value
    import capo_sagemaker.types.string_parameter_value

ArtifactProperties: TypeAlias = dict[
    "capo_sagemaker.types.string_parameter_value.StringParameterValue",
    "capo_sagemaker.types.artifact_property_value.ArtifactPropertyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ArtifactProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactProperties:
    out: ArtifactProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
