"""Generated from Smithy shape ``com.amazonaws.inspector#Subscription``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.event_subscription_list


class Subscription(TypedDict):
    resource_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template that is used during the event for which the SNS notification is sent.</p>"""
    topic_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS notifications are sent.</p>"""
    event_subscriptions: (
        "aws_sdk_inspector.types.event_subscription_list.EventSubscriptionList"
    )
    """<p>The list of existing event subscriptions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subscription) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["topicArn"] = value["topic_arn"]
    import aws_sdk_inspector.types.event_subscription_list

    out["eventSubscriptions"] = (
        aws_sdk_inspector.types.event_subscription_list.serialize_aws_json_1_1(
            value["event_subscriptions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("Subscription.resource_arn required")
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    else:
        raise DeserializationError("Subscription.topic_arn required")
    if "eventSubscriptions" in data:
        import aws_sdk_inspector.types.event_subscription_list

        out["event_subscriptions"] = (
            aws_sdk_inspector.types.event_subscription_list.deserialize_aws_json_1_1(
                data["eventSubscriptions"]
            )
        )
    else:
        raise DeserializationError("Subscription.event_subscriptions required")
    return out
