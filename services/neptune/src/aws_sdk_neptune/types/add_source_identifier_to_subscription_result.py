"""Generated from Smithy shape ``com.amazonaws.neptune#AddSourceIdentifierToSubscriptionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.event_subscription


class AddSourceIdentifierToSubscriptionResult(TypedDict):
    event_subscription: NotRequired[
        "aws_sdk_neptune.types.event_subscription.EventSubscription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AddSourceIdentifierToSubscriptionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "event_subscription" in value:
        import aws_sdk_neptune.types.event_subscription

        aws_sdk_neptune.types.event_subscription.serialize_query(
            value["event_subscription"], pairs, f"{prefix}.EventSubscription"
        )


def deserialize_query(el: Element) -> AddSourceIdentifierToSubscriptionResult:
    out: AddSourceIdentifierToSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_event_subscription = el.find("EventSubscription")
    if child_event_subscription is not None:
        import aws_sdk_neptune.types.event_subscription

        out["event_subscription"] = (
            aws_sdk_neptune.types.event_subscription.deserialize_query(
                child_event_subscription
            )
        )
    return out
