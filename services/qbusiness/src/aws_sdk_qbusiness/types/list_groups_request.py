"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_groups_request
    import aws_sdk_qbusiness.types.next_token
    import aws_sdk_qbusiness.types.timestamp


class ListGroupsRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application for getting a list of groups mapped to users.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index for getting a list of groups mapped to users.</p>"""
    updated_earlier_than: "aws_sdk_qbusiness.types.timestamp.Timestamp"
    """<p>The timestamp identifier used for the latest <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>"""
    data_source_id: NotRequired["aws_sdk_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source for getting a list of groups mapped to users.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of groups that are mapped to users.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_groups_request.MaxResultsIntegerForListGroupsRequest"
    ]
    """<p>The maximum number of returned groups that are mapped to users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGroupsRequest:
    out: ListGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
