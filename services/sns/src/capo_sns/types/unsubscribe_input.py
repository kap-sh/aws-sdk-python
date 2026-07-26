"""Generated from Smithy shape ``com.amazonaws.sns#UnsubscribeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.subscription_arn


class UnsubscribeInput(TypedDict, closed=True):
    subscription_arn: "capo_sns.types.subscription_arn.subscriptionARN"
    """<p>The ARN of the subscription to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UnsubscribeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SubscriptionArn", str(value["subscription_arn"])))


def deserialize_query(el: Element) -> UnsubscribeInput:
    out: UnsubscribeInput = {}  # type: ignore[typeddict-item]
    child_subscription_arn = el.find("SubscriptionArn")
    if child_subscription_arn is not None:
        out["subscription_arn"] = str(child_subscription_arn.text or "")
    else:
        raise DeserializationError("UnsubscribeInput.subscription_arn required")
    return out
