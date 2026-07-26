"""Generated from Smithy shape ``com.amazonaws.batch#EksAttemptDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.eks_attempt_detail

EksAttemptDetails: TypeAlias = list[
    "capo_batch.types.eks_attempt_detail.EksAttemptDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAttemptDetails) -> list:
    import capo_batch.types.eks_attempt_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.eks_attempt_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksAttemptDetails:
    import capo_batch.types.eks_attempt_detail

    out: EksAttemptDetails = []
    for item in data:
        out.append(capo_batch.types.eks_attempt_detail.deserialize_json(item))
    return out
