"""Generated from Smithy shape ``com.amazonaws.datazone#ListProjectMembershipsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.sort_field_project
    import aws_sdk_datazone.types.sort_order


class ListProjectMembershipsInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which you want to list project memberships.</p>"""
    project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project whose memberships you want to list.</p>"""
    sort_by: NotRequired["aws_sdk_datazone.types.sort_field_project.SortFieldProject"]
    """<p>The method by which you want to sort the project memberships.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>The sort order of the project memberships.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of memberships is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of memberships, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListProjectMemberships</code> to list the next set of memberships.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of memberships to return in a single call to <code>ListProjectMemberships</code>. When the number of memberships to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListProjectMemberships</code> to list the next set of memberships.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectMembershipsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProjectMembershipsInput:
    out: ListProjectMembershipsInput = {}  # type: ignore[typeddict-item]
    return out
