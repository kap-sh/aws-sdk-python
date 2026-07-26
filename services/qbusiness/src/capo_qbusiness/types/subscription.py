"""Generated from Smithy shape ``com.amazonaws.qbusiness#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.subscription_arn
    import capo_qbusiness.types.subscription_details
    import capo_qbusiness.types.subscription_id
    import capo_qbusiness.types.subscription_principal


class Subscription(TypedDict, closed=True):
    subscription_id: NotRequired["capo_qbusiness.types.subscription_id.SubscriptionId"]
    """<p>The identifier of the Amazon Q Business subscription to be updated.</p>"""
    subscription_arn: NotRequired[
        "capo_qbusiness.types.subscription_arn.SubscriptionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Business subscription that was updated.</p>"""
    principal: NotRequired[
        "capo_qbusiness.types.subscription_principal.SubscriptionPrincipal"
    ]
    """<p>The IAM Identity Center <code>UserId</code> or <code>GroupId</code> of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application.</p>"""
    current_subscription: NotRequired[
        "capo_qbusiness.types.subscription_details.SubscriptionDetails"
    ]
    """<p>The type of your current Amazon Q Business subscription.</p>"""
    next_subscription: NotRequired[
        "capo_qbusiness.types.subscription_details.SubscriptionDetails"
    ]
    """<p>The type of the Amazon Q Business subscription for the next month.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Subscription) -> dict:
    out: dict = {}
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    if "subscription_arn" in value:
        out["subscriptionArn"] = value["subscription_arn"]
    if "principal" in value:
        import capo_qbusiness.types.subscription_principal

        out["principal"] = capo_qbusiness.types.subscription_principal.serialize_json(
            value["principal"]
        )
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


def deserialize_json(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if "subscriptionId" in data:
        out["subscription_id"] = data["subscriptionId"]
    if "subscriptionArn" in data:
        out["subscription_arn"] = data["subscriptionArn"]
    if "principal" in data:
        import capo_qbusiness.types.subscription_principal

        out["principal"] = capo_qbusiness.types.subscription_principal.deserialize_json(
            data["principal"]
        )
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
