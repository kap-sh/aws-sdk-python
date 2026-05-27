"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionStatusValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.eks_anywhere_subscription_status

EksAnywhereSubscriptionStatusValues: TypeAlias = list[
    "aws_sdk_eks.types.eks_anywhere_subscription_status.EksAnywhereSubscriptionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscriptionStatusValues) -> list:
    import aws_sdk_eks.types.eks_anywhere_subscription_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_eks.types.eks_anywhere_subscription_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EksAnywhereSubscriptionStatusValues:
    import aws_sdk_eks.types.eks_anywhere_subscription_status

    out: EksAnywhereSubscriptionStatusValues = []
    for item in data:
        out.append(
            aws_sdk_eks.types.eks_anywhere_subscription_status.deserialize_json(item)
        )
    return out
