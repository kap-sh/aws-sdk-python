"""Generated from Smithy shape ``com.amazonaws.neptune#RemoveSourceIdentifierFromSubscriptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.event_subscription


class RemoveSourceIdentifierFromSubscriptionResult(TypedDict, closed=True):
    event_subscription: NotRequired[
        "capo_neptune.types.event_subscription.EventSubscription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveSourceIdentifierFromSubscriptionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "event_subscription" in value:
        import capo_neptune.types.event_subscription

        capo_neptune.types.event_subscription.serialize_query(
            value["event_subscription"], pairs, f"{prefix}.EventSubscription"
        )


def deserialize_query(el: Element) -> RemoveSourceIdentifierFromSubscriptionResult:
    out: RemoveSourceIdentifierFromSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_event_subscription = el.find("EventSubscription")
    if child_event_subscription is not None:
        import capo_neptune.types.event_subscription

        out["event_subscription"] = (
            capo_neptune.types.event_subscription.deserialize_query(
                child_event_subscription
            )
        )
    return out
