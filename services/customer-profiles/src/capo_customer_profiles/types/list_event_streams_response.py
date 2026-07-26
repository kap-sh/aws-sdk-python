"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListEventStreamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_stream_summary_list
    import capo_customer_profiles.types.token


class ListEventStreamsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_customer_profiles.types.event_stream_summary_list.EventStreamSummaryList"
    ]
    """<p>Contains summary information about an EventStream.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>Identifies the next page of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventStreamsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_customer_profiles.types.event_stream_summary_list

        out["Items"] = (
            capo_customer_profiles.types.event_stream_summary_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventStreamsResponse:
    out: ListEventStreamsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_customer_profiles.types.event_stream_summary_list

        out["items"] = (
            capo_customer_profiles.types.event_stream_summary_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
