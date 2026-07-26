"""Generated from Smithy shape ``com.amazonaws.connect#ListQueuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.queue_summary_list


class ListQueuesResponse(TypedDict, closed=True):
    queue_summary_list: NotRequired[
        "capo_connect.types.queue_summary_list.QueueSummaryList"
    ]
    """<p>Information about the queues.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueuesResponse) -> dict:
    out: dict = {}
    if "queue_summary_list" in value:
        import capo_connect.types.queue_summary_list

        out["QueueSummaryList"] = capo_connect.types.queue_summary_list.serialize_json(
            value["queue_summary_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQueuesResponse:
    out: ListQueuesResponse = {}  # type: ignore[typeddict-item]
    if "QueueSummaryList" in data:
        import capo_connect.types.queue_summary_list

        out["queue_summary_list"] = (
            capo_connect.types.queue_summary_list.deserialize_json(
                data["QueueSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
