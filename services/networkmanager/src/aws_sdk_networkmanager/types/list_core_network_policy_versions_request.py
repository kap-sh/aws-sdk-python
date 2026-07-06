"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworkPolicyVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token


class ListCoreNetworkPolicyVersionsRequest(TypedDict, closed=True):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network.</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkPolicyVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCoreNetworkPolicyVersionsRequest:
    out: ListCoreNetworkPolicyVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
