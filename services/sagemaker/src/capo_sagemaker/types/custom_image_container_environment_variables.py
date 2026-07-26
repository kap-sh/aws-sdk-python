"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomImageContainerEnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.non_empty_string256
    import capo_sagemaker.types.string256

CustomImageContainerEnvironmentVariables: TypeAlias = dict[
    "capo_sagemaker.types.non_empty_string256.NonEmptyString256",
    "capo_sagemaker.types.string256.String256",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: CustomImageContainerEnvironmentVariables,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomImageContainerEnvironmentVariables:
    out: CustomImageContainerEnvironmentVariables = {}
    for key, value in data.items():
        out[key] = value
    return out
