"""Generated from Smithy shape ``com.amazonaws.rds#EventSubscriptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.event_subscription

EventSubscriptionsList: TypeAlias = list[
    "capo_rds.types.event_subscription.EventSubscription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventSubscriptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.event_subscription

    for n, item in enumerate(value, 1):
        capo_rds.types.event_subscription.serialize_query(
            item, pairs, f"{prefix}.EventSubscription.{n}"
        )


def deserialize_query(el: Element) -> EventSubscriptionsList:
    import capo_rds.types.event_subscription

    out: EventSubscriptionsList = []
    for child in el.findall("EventSubscription"):
        out.append(capo_rds.types.event_subscription.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EventSubscriptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.event_subscription

    for n, item in enumerate(value, 1):
        capo_rds.types.event_subscription.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> EventSubscriptionsList:
    import capo_rds.types.event_subscription

    out: EventSubscriptionsList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.event_subscription.deserialize_query(child))
    return out
