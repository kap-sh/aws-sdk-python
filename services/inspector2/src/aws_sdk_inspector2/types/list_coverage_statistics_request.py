"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCoverageStatisticsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.coverage_filter_criteria
    import aws_sdk_inspector2.types.group_key
    import aws_sdk_inspector2.types.next_token


class ListCoverageStatisticsRequest(TypedDict):
    filter_criteria: NotRequired[
        "aws_sdk_inspector2.types.coverage_filter_criteria.CoverageFilterCriteria"
    ]
    """<p>An object that contains details on the filters to apply to the coverage data for your environment.</p>"""
    group_by: NotRequired["aws_sdk_inspector2.types.group_key.GroupKey"]
    """<p>The value to group the results by.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoverageStatisticsRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import aws_sdk_inspector2.types.coverage_filter_criteria

        out["filterCriteria"] = (
            aws_sdk_inspector2.types.coverage_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "group_by" in value:
        out["groupBy"] = value["group_by"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoverageStatisticsRequest:
    out: ListCoverageStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.coverage_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.coverage_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "groupBy" in data:
        out["group_by"] = data["groupBy"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
