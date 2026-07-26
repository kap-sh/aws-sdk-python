"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.eks_container_detail

EksContainerDetails: TypeAlias = list[
    "capo_batch.types.eks_container_detail.EksContainerDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerDetails) -> list:
    import capo_batch.types.eks_container_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.eks_container_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksContainerDetails:
    import capo_batch.types.eks_container_detail

    out: EksContainerDetails = []
    for item in data:
        out.append(capo_batch.types.eks_container_detail.deserialize_json(item))
    return out
