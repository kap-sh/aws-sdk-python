"""Generated from Smithy shape ``com.amazonaws.connect#SearchWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result500
    import aws_sdk_connect.types.next_token2500
    import aws_sdk_connect.types.workspace_search_criteria
    import aws_sdk_connect.types.workspace_search_filter


class SearchWorkspacesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result500.MaxResult500"]
    """<p>The maximum number of results to return per page.</p>"""
    search_filter: NotRequired[
        "aws_sdk_connect.types.workspace_search_filter.WorkspaceSearchFilter"
    ]
    """<p>Filters to apply to the search, such as tag-based filters.</p>"""
    search_criteria: NotRequired[
        "aws_sdk_connect.types.workspace_search_criteria.WorkspaceSearchCriteria"
    ]
    """<p>The search criteria, including field names and comparison types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchWorkspacesRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "search_filter" in value:
        import aws_sdk_connect.types.workspace_search_filter

        out["SearchFilter"] = (
            aws_sdk_connect.types.workspace_search_filter.serialize_json(
                value["search_filter"]
            )
        )
    if "search_criteria" in value:
        import aws_sdk_connect.types.workspace_search_criteria

        out["SearchCriteria"] = (
            aws_sdk_connect.types.workspace_search_criteria.serialize_json(
                value["search_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchWorkspacesRequest:
    out: SearchWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("SearchWorkspacesRequest.instance_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "SearchFilter" in data:
        import aws_sdk_connect.types.workspace_search_filter

        out["search_filter"] = (
            aws_sdk_connect.types.workspace_search_filter.deserialize_json(
                data["SearchFilter"]
            )
        )
    if "SearchCriteria" in data:
        import aws_sdk_connect.types.workspace_search_criteria

        out["search_criteria"] = (
            aws_sdk_connect.types.workspace_search_criteria.deserialize_json(
                data["SearchCriteria"]
            )
        )
    return out
