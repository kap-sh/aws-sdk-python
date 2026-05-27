"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayPrefixListReferencesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference_set


class GetTransitGatewayPrefixListReferencesResult(TypedDict):
    transit_gateway_prefix_list_references: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_prefix_list_reference_set.TransitGatewayPrefixListReferenceSet"
    ]
    """<p>Information about the prefix list references.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
