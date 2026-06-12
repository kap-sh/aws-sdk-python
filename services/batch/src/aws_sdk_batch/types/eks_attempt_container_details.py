"""Generated from Smithy shape ``com.amazonaws.batch#EksAttemptContainerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_attempt_container_detail

EksAttemptContainerDetails: TypeAlias = list[
    "aws_sdk_batch.types.eks_attempt_container_detail.EksAttemptContainerDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAttemptContainerDetails) -> list:
    import aws_sdk_batch.types.eks_attempt_container_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_batch.types.eks_attempt_container_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EksAttemptContainerDetails:
    import aws_sdk_batch.types.eks_attempt_container_detail

    out: EksAttemptContainerDetails = []
    for item in data:
        out.append(
            aws_sdk_batch.types.eks_attempt_container_detail.deserialize_json(item)
        )
    return out
