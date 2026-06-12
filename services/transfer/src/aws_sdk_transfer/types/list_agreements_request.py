"""Generated from Smithy shape ``com.amazonaws.transfer#ListAgreementsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.max_results
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.server_id


class ListAgreementsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_transfer.types.max_results.MaxResults"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListAgreements</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional agreements.</p>"""
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>The identifier of the server for which you want a list of agreements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAgreementsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAgreementsRequest:
    out: ListAgreementsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ListAgreementsRequest.server_id required")
    return out
