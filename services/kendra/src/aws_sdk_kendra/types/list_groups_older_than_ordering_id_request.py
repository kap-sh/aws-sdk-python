"""Generated from Smithy shape ``com.amazonaws.kendra#ListGroupsOlderThanOrderingIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.max_results_integer_for_list_principals_request
    import aws_sdk_kendra.types.next_token
    import aws_sdk_kendra.types.principal_ordering_id


class ListGroupsOlderThanOrderingIdRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for getting a list of groups mapped to users before a given ordering or timestamp identifier.</p>"""
    data_source_id: NotRequired["aws_sdk_kendra.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source for getting a list of groups mapped to users before a given ordering timestamp identifier.</p>"""
    ordering_id: "aws_sdk_kendra.types.principal_ordering_id.PrincipalOrderingId"
    """<p>The timestamp identifier used for the latest <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p> If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of groups that are mapped to users before a given ordering or timestamp identifier. </p>"""
    max_results: NotRequired[
        "aws_sdk_kendra.types.max_results_integer_for_list_principals_request.MaxResultsIntegerForListPrincipalsRequest"
    ]
    """<p> The maximum number of returned groups that are mapped to users before a given ordering or timestamp identifier. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsOlderThanOrderingIdRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    out["OrderingId"] = value["ordering_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsOlderThanOrderingIdRequest:
    out: ListGroupsOlderThanOrderingIdRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "ListGroupsOlderThanOrderingIdRequest.index_id required"
        )
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "OrderingId" in data:
        out["ordering_id"] = data["OrderingId"]
    else:
        raise DeserializationError(
            "ListGroupsOlderThanOrderingIdRequest.ordering_id required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
