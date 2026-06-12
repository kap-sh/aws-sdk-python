"""Generated from Smithy shape ``com.amazonaws.batch#EksContainers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_container

EksContainers: TypeAlias = list["aws_sdk_batch.types.eks_container.EksContainer"]


# --- restJson1 ser/de ---
def serialize_json(value: EksContainers) -> list:
    import aws_sdk_batch.types.eks_container

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.eks_container.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksContainers:
    import aws_sdk_batch.types.eks_container

    out: EksContainers = []
    for item in data:
        out.append(aws_sdk_batch.types.eks_container.deserialize_json(item))
    return out
