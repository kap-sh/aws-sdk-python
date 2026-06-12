"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerEnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_container_environment_variable

EksContainerEnvironmentVariables: TypeAlias = list[
    "aws_sdk_batch.types.eks_container_environment_variable.EksContainerEnvironmentVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerEnvironmentVariables) -> list:
    import aws_sdk_batch.types.eks_container_environment_variable

    out: list = []
    for item in value:
        out.append(
            aws_sdk_batch.types.eks_container_environment_variable.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EksContainerEnvironmentVariables:
    import aws_sdk_batch.types.eks_container_environment_variable

    out: EksContainerEnvironmentVariables = []
    for item in data:
        out.append(
            aws_sdk_batch.types.eks_container_environment_variable.deserialize_json(
                item
            )
        )
    return out
