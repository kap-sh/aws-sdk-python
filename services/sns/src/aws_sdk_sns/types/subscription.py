"""Generated from Smithy shape ``com.amazonaws.sns#Subscription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.account
    import aws_sdk_sns.types.endpoint2
    import aws_sdk_sns.types.protocol
    import aws_sdk_sns.types.subscription_arn
    import aws_sdk_sns.types.topic_arn


class Subscription(TypedDict):
    subscription_arn: NotRequired["aws_sdk_sns.types.subscription_arn.subscriptionARN"]
    """<p>The subscription's ARN.</p>"""
    owner: NotRequired["aws_sdk_sns.types.account.account"]
    """<p>The subscription's owner.</p>"""
    protocol: NotRequired["aws_sdk_sns.types.protocol.protocol"]
    """<p>The subscription's protocol.</p>"""
    endpoint: NotRequired["aws_sdk_sns.types.endpoint2.Endpoint2"]
    """<p>The subscription's endpoint (format depends on the protocol).</p>"""
    topic_arn: NotRequired["aws_sdk_sns.types.topic_arn.topicARN"]
    """<p>The ARN of the subscription's topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Subscription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subscription_arn" in value:
        pairs.append((f"{prefix}.SubscriptionArn", str(value["subscription_arn"])))
    if "owner" in value:
        pairs.append((f"{prefix}.Owner", str(value["owner"])))
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))
    if "endpoint" in value:
        pairs.append((f"{prefix}.Endpoint", str(value["endpoint"])))
    if "topic_arn" in value:
        pairs.append((f"{prefix}.TopicArn", str(value["topic_arn"])))


def deserialize_query(el: Element) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    child_subscription_arn = el.find("SubscriptionArn")
    if child_subscription_arn is not None:
        out["subscription_arn"] = str(child_subscription_arn.text or "")
    child_owner = el.find("Owner")
    if child_owner is not None:
        out["owner"] = str(child_owner.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    return out
