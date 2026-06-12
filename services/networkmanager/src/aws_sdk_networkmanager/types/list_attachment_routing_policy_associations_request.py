"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListAttachmentRoutingPolicyAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token


class ListAttachmentRoutingPolicyAssociationsRequest(TypedDict):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network to list attachment routing policy associations for.</p>"""
    attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of a specific attachment to filter the routing policy associations.</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single page.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentRoutingPolicyAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAttachmentRoutingPolicyAssociationsRequest:
    out: ListAttachmentRoutingPolicyAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
