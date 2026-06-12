"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.marker_type
    import aws_sdk_workdocs.types.positive_integer_type
    import aws_sdk_workdocs.types.search_query_type


class DescribeGroupsRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    search_query: "aws_sdk_workdocs.types.search_query_type.SearchQueryType"
    """<p>A query to describe groups by group name.</p>"""
    organization_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.marker_type.MarkerType"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    limit: NotRequired[
        "aws_sdk_workdocs.types.positive_integer_type.PositiveIntegerType"
    ]
    """<p>The maximum number of items to return with this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGroupsRequest:
    out: DescribeGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
