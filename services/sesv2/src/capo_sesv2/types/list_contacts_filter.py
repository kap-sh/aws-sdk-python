"""Generated from Smithy shape ``com.amazonaws.sesv2#ListContactsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.subscription_status
    import capo_sesv2.types.topic_filter


class ListContactsFilter(TypedDict, closed=True):
    filtered_status: NotRequired[
        "capo_sesv2.types.subscription_status.SubscriptionStatus"
    ]
    """<p>The status by which you are filtering: <code>OPT_IN</code> or <code>OPT_OUT</code>.</p>"""
    topic_filter: NotRequired["capo_sesv2.types.topic_filter.TopicFilter"]
    """<p>Used for filtering by a specific topic preference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactsFilter) -> dict:
    out: dict = {}
    if "filtered_status" in value:
        import capo_sesv2.types.subscription_status

        out["FilteredStatus"] = capo_sesv2.types.subscription_status.serialize_json(
            value["filtered_status"]
        )
    if "topic_filter" in value:
        import capo_sesv2.types.topic_filter

        out["TopicFilter"] = capo_sesv2.types.topic_filter.serialize_json(
            value["topic_filter"]
        )
    return out


def deserialize_json(data: dict) -> ListContactsFilter:
    out: ListContactsFilter = {}  # type: ignore[typeddict-item]
    if "FilteredStatus" in data:
        import capo_sesv2.types.subscription_status

        out["filtered_status"] = capo_sesv2.types.subscription_status.deserialize_json(
            data["FilteredStatus"]
        )
    if "TopicFilter" in data:
        import capo_sesv2.types.topic_filter

        out["topic_filter"] = capo_sesv2.types.topic_filter.deserialize_json(
            data["TopicFilter"]
        )
    return out
