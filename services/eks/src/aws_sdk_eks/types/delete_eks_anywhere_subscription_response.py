"""Generated from Smithy shape ``com.amazonaws.eks#DeleteEksAnywhereSubscriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.eks_anywhere_subscription


class DeleteEksAnywhereSubscriptionResponse(TypedDict):
    subscription: NotRequired[
        "aws_sdk_eks.types.eks_anywhere_subscription.EksAnywhereSubscription"
    ]
    """<p>The full description of the subscription to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEksAnywhereSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription" in value:
        import aws_sdk_eks.types.eks_anywhere_subscription

        out["subscription"] = (
            aws_sdk_eks.types.eks_anywhere_subscription.serialize_json(
                value["subscription"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteEksAnywhereSubscriptionResponse:
    out: DeleteEksAnywhereSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "subscription" in data:
        import aws_sdk_eks.types.eks_anywhere_subscription

        out["subscription"] = (
            aws_sdk_eks.types.eks_anywhere_subscription.deserialize_json(
                data["subscription"]
            )
        )
    return out
