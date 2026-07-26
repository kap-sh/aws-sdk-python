"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.eks_anywhere_subscription

EksAnywhereSubscriptionList: TypeAlias = list[
    "capo_eks.types.eks_anywhere_subscription.EksAnywhereSubscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscriptionList) -> list:
    import capo_eks.types.eks_anywhere_subscription

    out: list = []
    for item in value:
        out.append(capo_eks.types.eks_anywhere_subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksAnywhereSubscriptionList:
    import capo_eks.types.eks_anywhere_subscription

    out: EksAnywhereSubscriptionList = []
    for item in data:
        out.append(capo_eks.types.eks_anywhere_subscription.deserialize_json(item))
    return out
