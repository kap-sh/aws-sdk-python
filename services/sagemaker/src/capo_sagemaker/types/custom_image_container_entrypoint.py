"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomImageContainerEntrypoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.non_empty_string256

CustomImageContainerEntrypoint: TypeAlias = list[
    "capo_sagemaker.types.non_empty_string256.NonEmptyString256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomImageContainerEntrypoint) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomImageContainerEntrypoint:
    return list(data)
