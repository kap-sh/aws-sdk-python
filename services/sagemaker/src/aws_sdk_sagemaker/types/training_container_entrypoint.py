"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingContainerEntrypoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_container_entrypoint_string

TrainingContainerEntrypoint: TypeAlias = list[
    "aws_sdk_sagemaker.types.training_container_entrypoint_string.TrainingContainerEntrypointString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingContainerEntrypoint) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TrainingContainerEntrypoint:
    return list(data)
