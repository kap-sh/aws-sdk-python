"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListProjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.project_list_filters


class ListProjectsRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""
    filters: NotRequired[
        "capo_codecatalyst.types.project_list_filters.ProjectListFilters"
    ]
    """<p>Information about filters to apply to narrow the results returned in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_codecatalyst.types.project_list_filters

        out["filters"] = capo_codecatalyst.types.project_list_filters.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListProjectsRequest:
    out: ListProjectsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import capo_codecatalyst.types.project_list_filters

        out["filters"] = capo_codecatalyst.types.project_list_filters.deserialize_json(
            data["filters"]
        )
    return out
