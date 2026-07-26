"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListEventTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.list_event_types_filters
    import capo_codestar_notifications.types.max_results
    import capo_codestar_notifications.types.next_token


class ListEventTypesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_codestar_notifications.types.list_event_types_filters.ListEventTypesFilters"
    ]
    """<p>The filters to use to return information by service or resource type.</p>"""
    next_token: NotRequired["capo_codestar_notifications.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""
    max_results: NotRequired["capo_codestar_notifications.types.max_results.MaxResults"]
    """<p>A non-negative integer used to limit the number of returned results. The default number is 50. The maximum number of results that can be returned is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventTypesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_codestar_notifications.types.list_event_types_filters

        out["Filters"] = (
            capo_codestar_notifications.types.list_event_types_filters.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListEventTypesRequest:
    out: ListEventTypesRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_codestar_notifications.types.list_event_types_filters

        out["filters"] = (
            capo_codestar_notifications.types.list_event_types_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
