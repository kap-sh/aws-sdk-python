"""Generated from Smithy shape ``com.amazonaws.eks#CreateEksAnywhereSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.eks_anywhere_subscription


class CreateEksAnywhereSubscriptionResponse(TypedDict, closed=True):
    subscription: NotRequired[
        "aws_sdk_eks.types.eks_anywhere_subscription.EksAnywhereSubscription"
    ]
    """<p>The full description of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEksAnywhereSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription" in value:
        import aws_sdk_eks.types.eks_anywhere_subscription

        out["subscription"] = (
            aws_sdk_eks.types.eks_anywhere_subscription.serialize_json(
                value["subscription"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateEksAnywhereSubscriptionResponse:
    out: CreateEksAnywhereSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "subscription" in data:
        import aws_sdk_eks.types.eks_anywhere_subscription

        out["subscription"] = (
            aws_sdk_eks.types.eks_anywhere_subscription.deserialize_json(
                data["subscription"]
            )
        )
    return out
