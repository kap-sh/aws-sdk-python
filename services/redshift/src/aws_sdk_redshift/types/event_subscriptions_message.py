"""Generated from Smithy shape ``com.amazonaws.redshift#EventSubscriptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.event_subscriptions_list
    import aws_sdk_redshift.types.string


class EventSubscriptionsMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    event_subscriptions_list: NotRequired[
        "aws_sdk_redshift.types.event_subscriptions_list.EventSubscriptionsList"
    ]
    """<p>A list of event subscriptions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventSubscriptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "event_subscriptions_list" in value:
        import aws_sdk_redshift.types.event_subscriptions_list

        aws_sdk_redshift.types.event_subscriptions_list.serialize_query(
            value["event_subscriptions_list"], pairs, f"{prefix}.EventSubscriptionsList"
        )


def deserialize_query(el: Element) -> EventSubscriptionsMessage:
    out: EventSubscriptionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_event_subscriptions_list = el.find("EventSubscriptionsList")
    if child_event_subscriptions_list is not None:
        import aws_sdk_redshift.types.event_subscriptions_list

        out["event_subscriptions_list"] = (
            aws_sdk_redshift.types.event_subscriptions_list.deserialize_query(
                child_event_subscriptions_list
            )
        )
    return out
