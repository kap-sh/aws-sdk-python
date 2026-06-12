"""Generated from Smithy shape ``com.amazonaws.fms#ListProtocolsListsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.pagination_max_results
    import aws_sdk_fms.types.pagination_token


class ListProtocolsListsRequest(TypedDict):
    default_lists: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Specifies whether the lists to retrieve are default lists owned by Firewall Manager.</p>"""
    next_token: NotRequired["aws_sdk_fms.types.pagination_token.PaginationToken"]
    """<p>If you specify a value for <code>MaxResults</code> in your list request, and you have more objects than the maximum, Firewall Manager returns this token in the response. For all but the first request, you provide the token returned by the prior request in the request parameters, to retrieve the next batch of objects.</p>"""
    max_results: "aws_sdk_fms.types.pagination_max_results.PaginationMaxResults"
    """<p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify this, Firewall Manager returns all available objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProtocolsListsRequest) -> dict:
    out: dict = {}
    out["DefaultLists"] = value.get("default_lists", False)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProtocolsListsRequest:
    out: ListProtocolsListsRequest = {}  # type: ignore[typeddict-item]
    if "DefaultLists" in data:
        out["default_lists"] = data["DefaultLists"]
    else:
        out["default_lists"] = False
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        raise DeserializationError("ListProtocolsListsRequest.max_results required")
    return out
