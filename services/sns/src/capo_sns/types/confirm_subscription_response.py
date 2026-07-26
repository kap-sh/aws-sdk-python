"""Generated from Smithy shape ``com.amazonaws.sns#ConfirmSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.subscription_arn


class ConfirmSubscriptionResponse(TypedDict, closed=True):
    subscription_arn: NotRequired["capo_sns.types.subscription_arn.subscriptionARN"]
    """<p>The ARN of the created subscription.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfirmSubscriptionResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subscription_arn" in value:
        pairs.append((f"{prefix}.SubscriptionArn", str(value["subscription_arn"])))


def deserialize_query(el: Element) -> ConfirmSubscriptionResponse:
    out: ConfirmSubscriptionResponse = {}  # type: ignore[typeddict-item]
    child_subscription_arn = el.find("SubscriptionArn")
    if child_subscription_arn is not None:
        out["subscription_arn"] = str(child_subscription_arn.text or "")
    return out
