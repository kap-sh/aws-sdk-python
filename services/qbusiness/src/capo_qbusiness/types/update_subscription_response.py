"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.subscription_arn
    import capo_qbusiness.types.subscription_details


class UpdateSubscriptionResponse(TypedDict, closed=True):
    subscription_arn: NotRequired[
        "capo_qbusiness.types.subscription_arn.SubscriptionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Business subscription that was updated.</p>"""
    current_subscription: NotRequired[
        "capo_qbusiness.types.subscription_details.SubscriptionDetails"
    ]
    """<p>The type of your current Amazon Q Business subscription.</p>"""
    next_subscription: NotRequired[
        "capo_qbusiness.types.subscription_details.SubscriptionDetails"
    ]
    """<p>The type of the Amazon Q Business subscription for the next month.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription_arn" in value:
        out["subscriptionArn"] = value["subscription_arn"]
    if "current_subscription" in value:
        import capo_qbusiness.types.subscription_details

        out["currentSubscription"] = (
            capo_qbusiness.types.subscription_details.serialize_json(
                value["current_subscription"]
            )
        )
    if "next_subscription" in value:
        import capo_qbusiness.types.subscription_details

        out["nextSubscription"] = (
            capo_qbusiness.types.subscription_details.serialize_json(
                value["next_subscription"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionResponse:
    out: UpdateSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "subscriptionArn" in data:
        out["subscription_arn"] = data["subscriptionArn"]
    if "currentSubscription" in data:
        import capo_qbusiness.types.subscription_details

        out["current_subscription"] = (
            capo_qbusiness.types.subscription_details.deserialize_json(
                data["currentSubscription"]
            )
        )
    if "nextSubscription" in data:
        import capo_qbusiness.types.subscription_details

        out["next_subscription"] = (
            capo_qbusiness.types.subscription_details.deserialize_json(
                data["nextSubscription"]
            )
        )
    return out
