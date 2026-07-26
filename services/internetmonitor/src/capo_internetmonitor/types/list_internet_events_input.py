"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListInternetEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_internetmonitor.types.internet_event_max_results


class ListInternetEventsInput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired[
        "capo_internetmonitor.types.internet_event_max_results.InternetEventMaxResults"
    ]
    """<p>The number of query results that you want to return with this call.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time of the time window that you want to get a list of internet events for.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the time window that you want to get a list of internet events for.</p>"""
    event_status: NotRequired["str"]
    """<p>The status of an internet event.</p>"""
    event_type: NotRequired["str"]
    """<p>The type of network impairment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInternetEventsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInternetEventsInput:
    out: ListInternetEventsInput = {}  # type: ignore[typeddict-item]
    return out
