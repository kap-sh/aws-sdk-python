"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomImageContainerArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.non_empty_string64

CustomImageContainerArguments: TypeAlias = list[
    "capo_sagemaker.types.non_empty_string64.NonEmptyString64"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomImageContainerArguments) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomImageContainerArguments:
    return list(data)
