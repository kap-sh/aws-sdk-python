"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContainerArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.container_argument

ContainerArguments: TypeAlias = list[
    "capo_sagemaker.types.container_argument.ContainerArgument"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerArguments) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ContainerArguments:
    return list(data)
