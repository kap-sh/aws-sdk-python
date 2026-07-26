"""Generated from Smithy shape ``com.amazonaws.rum#GetAppMonitorDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.event_data_list
    import capo_rum.types.token


class GetAppMonitorDataResponse(TypedDict, closed=True):
    events: NotRequired["capo_rum.types.event_data_list.EventDataList"]
    """<p>The events that RUM collected that match your request.</p>"""
    next_token: NotRequired["capo_rum.types.token.Token"]
    """<p>A token that you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppMonitorDataResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_rum.types.event_data_list

        out["Events"] = capo_rum.types.event_data_list.serialize_json(value["events"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetAppMonitorDataResponse:
    out: GetAppMonitorDataResponse = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import capo_rum.types.event_data_list

        out["events"] = capo_rum.types.event_data_list.deserialize_json(data["Events"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
