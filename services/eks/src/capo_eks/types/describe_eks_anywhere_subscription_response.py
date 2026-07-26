"""Generated from Smithy shape ``com.amazonaws.eks#DescribeEksAnywhereSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.eks_anywhere_subscription


class DescribeEksAnywhereSubscriptionResponse(TypedDict, closed=True):
    subscription: NotRequired[
        "capo_eks.types.eks_anywhere_subscription.EksAnywhereSubscription"
    ]
    """<p>The full description of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEksAnywhereSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription" in value:
        import capo_eks.types.eks_anywhere_subscription

        out["subscription"] = capo_eks.types.eks_anywhere_subscription.serialize_json(
            value["subscription"]
        )
    return out


def deserialize_json(data: dict) -> DescribeEksAnywhereSubscriptionResponse:
    out: DescribeEksAnywhereSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "subscription" in data:
        import capo_eks.types.eks_anywhere_subscription

        out["subscription"] = capo_eks.types.eks_anywhere_subscription.deserialize_json(
            data["subscription"]
        )
    return out
