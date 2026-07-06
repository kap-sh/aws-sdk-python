"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCoverageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.coverage_filter_criteria
    import aws_sdk_inspector2.types.list_coverage_max_results
    import aws_sdk_inspector2.types.next_token


class ListCoverageRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_inspector2.types.list_coverage_max_results.ListCoverageMaxResults"
    ]
    """<p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    filter_criteria: NotRequired[
        "aws_sdk_inspector2.types.coverage_filter_criteria.CoverageFilterCriteria"
    ]
    """<p>An object that contains details on the filters to apply to the coverage data for your environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoverageRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filter_criteria" in value:
        import aws_sdk_inspector2.types.coverage_filter_criteria

        out["filterCriteria"] = (
            aws_sdk_inspector2.types.coverage_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCoverageRequest:
    out: ListCoverageRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.coverage_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.coverage_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    return out
