"""Generated from Smithy shape ``com.amazonaws.transfer#ListUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.server_id


class ListUsersRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_transfer.types.max_results.MaxResults"]
    """<p>Specifies the number of users to return as a response to the <code>ListUsers</code> request.</p>"""
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>If there are additional results from the <code>ListUsers</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> to a subsequent <code>ListUsers</code> command, to continue listing additional users.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that has users assigned to it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersRequest:
    out: ListUsersRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ListUsersRequest.server_id required")
    return out
