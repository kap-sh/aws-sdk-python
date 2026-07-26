"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetInternetEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.internet_event_id


class GetInternetEventInput(TypedDict, closed=True):
    event_id: "capo_internetmonitor.types.internet_event_id.InternetEventId"
    """<p>The <code>EventId</code> of the internet event to return information for. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInternetEventInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInternetEventInput:
    out: GetInternetEventInput = {}  # type: ignore[typeddict-item]
    return out
