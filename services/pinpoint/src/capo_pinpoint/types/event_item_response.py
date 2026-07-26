"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string


class EventItemResponse(TypedDict, closed=True):
    message: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A custom message that's returned in the response as a result of processing the event.</p>"""
    status_code: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The status code that's returned in the response as a result of processing the event. Possible values are: 202, for events that were accepted; and, 400, for events that weren't valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventItemResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    return out


def deserialize_json(data: dict) -> EventItemResponse:
    out: EventItemResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "StatusCode" in data:
        out["status_code"] = data["StatusCode"]
    return out
