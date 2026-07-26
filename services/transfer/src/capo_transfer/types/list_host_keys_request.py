"""Generated from Smithy shape ``com.amazonaws.transfer#ListHostKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.server_id


class ListHostKeysRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_transfer.types.max_results.MaxResults"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>When there are additional results that were not returned, a <code>NextToken</code> parameter is returned. You can use that value for a subsequent call to <code>ListHostKeys</code> to continue listing results.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that contains the host keys that you want to view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHostKeysRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHostKeysRequest:
    out: ListHostKeysRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ListHostKeysRequest.server_id required")
    return out
