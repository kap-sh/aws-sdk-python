"""Generated from Smithy shape ``com.amazonaws.docdb#CreateEventSubscriptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.event_subscription


class CreateEventSubscriptionResult(TypedDict, closed=True):
    event_subscription: NotRequired[
        "capo_docdb.types.event_subscription.EventSubscription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateEventSubscriptionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "event_subscription" in value:
        import capo_docdb.types.event_subscription

        capo_docdb.types.event_subscription.serialize_query(
            value["event_subscription"], pairs, f"{prefix}.EventSubscription"
        )


def deserialize_query(el: Element) -> CreateEventSubscriptionResult:
    out: CreateEventSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_event_subscription = el.find("EventSubscription")
    if child_event_subscription is not None:
        import capo_docdb.types.event_subscription

        out["event_subscription"] = (
            capo_docdb.types.event_subscription.deserialize_query(
                child_event_subscription
            )
        )
    return out
