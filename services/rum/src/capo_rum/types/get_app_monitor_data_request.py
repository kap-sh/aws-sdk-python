"""Generated from Smithy shape ``com.amazonaws.rum#GetAppMonitorDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_name
    import capo_rum.types.max_query_results
    import capo_rum.types.query_filters
    import capo_rum.types.time_range
    import capo_rum.types.token


class GetAppMonitorDataRequest(TypedDict, closed=True):
    name: "capo_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the app monitor that collected the data that you want to retrieve.</p>"""
    time_range: "capo_rum.types.time_range.TimeRange"
    """<p>A structure that defines the time range that you want to retrieve results from.</p>"""
    filters: NotRequired["capo_rum.types.query_filters.QueryFilters"]
    """<p>An array of structures that you can use to filter the results to those that match one or more sets of key-value pairs that you specify.</p>"""
    max_results: "capo_rum.types.max_query_results.MaxQueryResults"
    """<p>The maximum number of results to return in one operation. </p>"""
    next_token: NotRequired["capo_rum.types.token.Token"]
    """<p>Use the token returned by the previous operation to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppMonitorDataRequest) -> dict:
    out: dict = {}
    import capo_rum.types.time_range

    out["TimeRange"] = capo_rum.types.time_range.serialize_json(value["time_range"])
    if "filters" in value:
        import capo_rum.types.query_filters

        out["Filters"] = capo_rum.types.query_filters.serialize_json(value["filters"])
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetAppMonitorDataRequest:
    out: GetAppMonitorDataRequest = {}  # type: ignore[typeddict-item]
    if "TimeRange" in data:
        import capo_rum.types.time_range

        out["time_range"] = capo_rum.types.time_range.deserialize_json(
            data["TimeRange"]
        )
    else:
        raise DeserializationError("GetAppMonitorDataRequest.time_range required")
    if "Filters" in data:
        import capo_rum.types.query_filters

        out["filters"] = capo_rum.types.query_filters.deserialize_json(data["Filters"])
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
