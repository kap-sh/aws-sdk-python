"""Generated from Smithy shape ``com.amazonaws.sns#GetSubscriptionAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.subscription_arn


class GetSubscriptionAttributesInput(TypedDict, closed=True):
    subscription_arn: "aws_sdk_sns.types.subscription_arn.subscriptionARN"
    """<p>The ARN of the subscription whose properties you want to get.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSubscriptionAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SubscriptionArn", str(value["subscription_arn"])))


def deserialize_query(el: Element) -> GetSubscriptionAttributesInput:
    out: GetSubscriptionAttributesInput = {}  # type: ignore[typeddict-item]
    child_subscription_arn = el.find("SubscriptionArn")
    if child_subscription_arn is not None:
        out["subscription_arn"] = str(child_subscription_arn.text or "")
    else:
        raise DeserializationError(
            "GetSubscriptionAttributesInput.subscription_arn required"
        )
    return out
