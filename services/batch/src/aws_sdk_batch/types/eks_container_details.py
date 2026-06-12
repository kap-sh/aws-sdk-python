"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_container_detail

EksContainerDetails: TypeAlias = list[
    "aws_sdk_batch.types.eks_container_detail.EksContainerDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerDetails) -> list:
    import aws_sdk_batch.types.eks_container_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.eks_container_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksContainerDetails:
    import aws_sdk_batch.types.eks_container_detail

    out: EksContainerDetails = []
    for item in data:
        out.append(aws_sdk_batch.types.eks_container_detail.deserialize_json(item))
    return out
