"""Generated from Smithy shape ``com.amazonaws.batch#EksAttemptContainerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.eks_attempt_container_detail

EksAttemptContainerDetails: TypeAlias = list[
    "capo_batch.types.eks_attempt_container_detail.EksAttemptContainerDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAttemptContainerDetails) -> list:
    import capo_batch.types.eks_attempt_container_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.eks_attempt_container_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksAttemptContainerDetails:
    import capo_batch.types.eks_attempt_container_detail

    out: EksAttemptContainerDetails = []
    for item in data:
        out.append(capo_batch.types.eks_attempt_container_detail.deserialize_json(item))
    return out
