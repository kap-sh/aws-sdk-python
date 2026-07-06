"""Generated from Smithy shape ``com.amazonaws.budgets#Subscriber``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.subscriber_address
    import aws_sdk_budgets.types.subscription_type


class Subscriber(TypedDict, closed=True):
    subscription_type: "aws_sdk_budgets.types.subscription_type.SubscriptionType"
    """<p>The type of notification that Amazon Web Services sends to a subscriber.</p>"""
    address: "aws_sdk_budgets.types.subscriber_address.SubscriberAddress"
    """<p>The address that Amazon Web Services sends budget notifications to, either an SNS topic or an email.</p> <p>When you create a subscriber, the value of <code>Address</code> can't contain line breaks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subscriber) -> dict:
    out: dict = {}
    import aws_sdk_budgets.types.subscription_type

    out["SubscriptionType"] = (
        aws_sdk_budgets.types.subscription_type.serialize_aws_json_1_1(
            value["subscription_type"]
        )
    )
    out["Address"] = value["address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Subscriber:
    out: Subscriber = {}  # type: ignore[typeddict-item]
    if "SubscriptionType" in data:
        import aws_sdk_budgets.types.subscription_type

        out["subscription_type"] = (
            aws_sdk_budgets.types.subscription_type.deserialize_aws_json_1_1(
                data["SubscriptionType"]
            )
        )
    else:
        raise DeserializationError("Subscriber.subscription_type required")
    if "Address" in data:
        out["address"] = data["Address"]
    else:
        raise DeserializationError("Subscriber.address required")
    return out
