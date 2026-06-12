"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_container_override

EksContainerOverrideList: TypeAlias = list[
    "aws_sdk_batch.types.eks_container_override.EksContainerOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerOverrideList) -> list:
    import aws_sdk_batch.types.eks_container_override

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.eks_container_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksContainerOverrideList:
    import aws_sdk_batch.types.eks_container_override

    out: EksContainerOverrideList = []
    for item in data:
        out.append(aws_sdk_batch.types.eks_container_override.deserialize_json(item))
    return out
