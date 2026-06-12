"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContainerEntrypoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.container_entrypoint_string

ContainerEntrypoint: TypeAlias = list[
    "aws_sdk_sagemaker.types.container_entrypoint_string.ContainerEntrypointString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerEntrypoint) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ContainerEntrypoint:
    return list(data)
