"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionStatusValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.eks_anywhere_subscription_status

EksAnywhereSubscriptionStatusValues: TypeAlias = list[
    "capo_eks.types.eks_anywhere_subscription_status.EksAnywhereSubscriptionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscriptionStatusValues) -> list:
    import capo_eks.types.eks_anywhere_subscription_status

    out: list = []
    for item in value:
        out.append(capo_eks.types.eks_anywhere_subscription_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksAnywhereSubscriptionStatusValues:
    import capo_eks.types.eks_anywhere_subscription_status

    out: EksAnywhereSubscriptionStatusValues = []
    for item in data:
        out.append(
            capo_eks.types.eks_anywhere_subscription_status.deserialize_json(item)
        )
    return out
