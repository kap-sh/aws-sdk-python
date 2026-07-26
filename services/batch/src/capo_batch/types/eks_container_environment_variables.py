"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerEnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.eks_container_environment_variable

EksContainerEnvironmentVariables: TypeAlias = list[
    "capo_batch.types.eks_container_environment_variable.EksContainerEnvironmentVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerEnvironmentVariables) -> list:
    import capo_batch.types.eks_container_environment_variable

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.eks_container_environment_variable.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EksContainerEnvironmentVariables:
    import capo_batch.types.eks_container_environment_variable

    out: EksContainerEnvironmentVariables = []
    for item in data:
        out.append(
            capo_batch.types.eks_container_environment_variable.deserialize_json(item)
        )
    return out
