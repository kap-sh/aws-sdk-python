"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworkPrefixListAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token
    import aws_sdk_networkmanager.types.prefix_list_arn


class ListCoreNetworkPrefixListAssociationsRequest(TypedDict):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network to list prefix list associations for.</p>"""
    prefix_list_arn: NotRequired[
        "aws_sdk_networkmanager.types.prefix_list_arn.PrefixListArn"
    ]
    """<p>The ARN of a specific prefix list to filter the associations.</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single page.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkPrefixListAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCoreNetworkPrefixListAssociationsRequest:
    out: ListCoreNetworkPrefixListAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
