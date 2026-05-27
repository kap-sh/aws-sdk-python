"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.eks_anywhere_subscription

EksAnywhereSubscriptionList: TypeAlias = list[
    "aws_sdk_eks.types.eks_anywhere_subscription.EksAnywhereSubscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscriptionList) -> list:
    import aws_sdk_eks.types.eks_anywhere_subscription

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.eks_anywhere_subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksAnywhereSubscriptionList:
    import aws_sdk_eks.types.eks_anywhere_subscription

    out: EksAnywhereSubscriptionList = []
    for item in data:
        out.append(aws_sdk_eks.types.eks_anywhere_subscription.deserialize_json(item))
    return out
