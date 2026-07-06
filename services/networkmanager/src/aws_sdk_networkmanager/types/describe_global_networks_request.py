"""Generated from Smithy shape ``com.amazonaws.networkmanager#DescribeGlobalNetworksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_id_list
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token


class DescribeGlobalNetworksRequest(TypedDict, closed=True):
    global_network_ids: NotRequired[
        "aws_sdk_networkmanager.types.global_network_id_list.GlobalNetworkIdList"
    ]
    """<p>The IDs of one or more global networks. The maximum is 10.</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGlobalNetworksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGlobalNetworksRequest:
    out: DescribeGlobalNetworksRequest = {}  # type: ignore[typeddict-item]
    return out
