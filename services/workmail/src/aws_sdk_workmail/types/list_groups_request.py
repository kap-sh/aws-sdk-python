"""Generated from Smithy shape ``com.amazonaws.workmail#ListGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.list_groups_filters
    import aws_sdk_workmail.types.max_results
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.organization_id


class ListGroupsRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the groups exist.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>"""
    max_results: NotRequired["aws_sdk_workmail.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    filters: NotRequired["aws_sdk_workmail.types.list_groups_filters.ListGroupsFilters"]
    """<p>Limit the search results based on the filter criteria. Only one filter per request is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_workmail.types.list_groups_filters

        out["Filters"] = (
            aws_sdk_workmail.types.list_groups_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsRequest:
    out: ListGroupsRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("ListGroupsRequest.organization_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filters" in data:
        import aws_sdk_workmail.types.list_groups_filters

        out["filters"] = (
            aws_sdk_workmail.types.list_groups_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
