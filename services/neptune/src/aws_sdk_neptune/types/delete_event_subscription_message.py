"""Generated from Smithy shape ``com.amazonaws.neptune#DeleteEventSubscriptionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string


class DeleteEventSubscriptionMessage(TypedDict):
    subscription_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the event notification subscription you want to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteEventSubscriptionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subscription_name" in value:
        pairs.append((f"{prefix}.SubscriptionName", str(value["subscription_name"])))


def deserialize_query(el: Element) -> DeleteEventSubscriptionMessage:
    out: DeleteEventSubscriptionMessage = {}  # type: ignore[typeddict-item]
    child_subscription_name = el.find("SubscriptionName")
    if child_subscription_name is not None:
        out["subscription_name"] = str(child_subscription_name.text or "")
    return out
