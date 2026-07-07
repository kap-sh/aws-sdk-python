"""Generated from Smithy shape ``com.amazonaws.docdb#AddSourceIdentifierToSubscriptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.event_subscription


class AddSourceIdentifierToSubscriptionResult(TypedDict, closed=True):
    event_subscription: NotRequired[
        "aws_sdk_docdb.types.event_subscription.EventSubscription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AddSourceIdentifierToSubscriptionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "event_subscription" in value:
        import aws_sdk_docdb.types.event_subscription

        aws_sdk_docdb.types.event_subscription.serialize_query(
            value["event_subscription"], pairs, f"{prefix}.EventSubscription"
        )


def deserialize_query(el: Element) -> AddSourceIdentifierToSubscriptionResult:
    out: AddSourceIdentifierToSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_event_subscription = el.find("EventSubscription")
    if child_event_subscription is not None:
        import aws_sdk_docdb.types.event_subscription

        out["event_subscription"] = (
            aws_sdk_docdb.types.event_subscription.deserialize_query(
                child_event_subscription
            )
        )
    return out
