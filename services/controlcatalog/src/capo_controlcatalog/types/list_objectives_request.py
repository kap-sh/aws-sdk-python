"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListObjectivesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.max_list_objectives_results
    import capo_controlcatalog.types.objective_filter
    import capo_controlcatalog.types.pagination_token


class ListObjectivesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_controlcatalog.types.max_list_objectives_results.MaxListObjectivesResults"
    ]
    """<p>The maximum number of results on a page or for an API request call.</p>"""
    next_token: NotRequired[
        "capo_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    objective_filter: NotRequired[
        "capo_controlcatalog.types.objective_filter.ObjectiveFilter"
    ]
    """<p>An optional filter that narrows the results to a specific domain.</p> <p>This filter allows you to specify one domain ARN at a time. Passing multiple ARNs in the <code>ObjectiveFilter</code> isn’t supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectivesRequest) -> dict:
    out: dict = {}
    if "objective_filter" in value:
        import capo_controlcatalog.types.objective_filter

        out["ObjectiveFilter"] = (
            capo_controlcatalog.types.objective_filter.serialize_json(
                value["objective_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListObjectivesRequest:
    out: ListObjectivesRequest = {}  # type: ignore[typeddict-item]
    if "ObjectiveFilter" in data:
        import capo_controlcatalog.types.objective_filter

        out["objective_filter"] = (
            capo_controlcatalog.types.objective_filter.deserialize_json(
                data["ObjectiveFilter"]
            )
        )
    return out
