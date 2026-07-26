"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListControlsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_filter
    import capo_controlcatalog.types.max_list_controls_results
    import capo_controlcatalog.types.pagination_token


class ListControlsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired[
        "capo_controlcatalog.types.max_list_controls_results.MaxListControlsResults"
    ]
    """<p>The maximum number of results on a page or for an API request call.</p>"""
    filter: NotRequired["capo_controlcatalog.types.control_filter.ControlFilter"]
    """<p>An optional filter that narrows the results to controls with specific implementation types or identifiers. If you don't provide a filter, the operation returns all available controls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_controlcatalog.types.control_filter

        out["Filter"] = capo_controlcatalog.types.control_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ListControlsRequest:
    out: ListControlsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import capo_controlcatalog.types.control_filter

        out["filter"] = capo_controlcatalog.types.control_filter.deserialize_json(
            data["Filter"]
        )
    return out
