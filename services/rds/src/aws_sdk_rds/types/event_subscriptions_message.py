"""Generated from Smithy shape ``com.amazonaws.rds#EventSubscriptionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.event_subscriptions_list
    import aws_sdk_rds.types.string


class EventSubscriptionsMessage(TypedDict):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    event_subscriptions_list: NotRequired[
        "aws_sdk_rds.types.event_subscriptions_list.EventSubscriptionsList"
    ]
    """<p>A list of EventSubscriptions data types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventSubscriptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "event_subscriptions_list" in value:
        import aws_sdk_rds.types.event_subscriptions_list

        aws_sdk_rds.types.event_subscriptions_list.serialize_query(
            value["event_subscriptions_list"], pairs, f"{prefix}.EventSubscriptionsList"
        )


def deserialize_query(el: Element) -> EventSubscriptionsMessage:
    out: EventSubscriptionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_event_subscriptions_list = el.find("EventSubscriptionsList")
    if child_event_subscriptions_list is not None:
        import aws_sdk_rds.types.event_subscriptions_list

        out["event_subscriptions_list"] = (
            aws_sdk_rds.types.event_subscriptions_list.deserialize_query(
                child_event_subscriptions_list
            )
        )
    return out
