"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayConnectsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id_string_list
    import aws_sdk_ec2.types.transit_gateway_max_results


class DescribeTransitGatewayConnectsRequest(TypedDict):
    transit_gateway_attachment_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id_string_list.TransitGatewayAttachmentIdStringList"
    ]
    """<p>The IDs of the attachments.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>options.protocol</code> - The tunnel protocol (<code>gre</code>).</p> </li> <li> <p> <code>state</code> - The state of the attachment (<code>initiating</code> | <code>initiatingRequest</code> | <code>pendingAcceptance</code> | <code>rollingBack</code> | <code>pending</code> | <code>available</code> | <code>modifying</code> | <code>deleting</code> | <code>deleted</code> | <code>failed</code> | <code>rejected</code> | <code>rejecting</code> | <code>failing</code>).</p> </li> <li> <p> <code>transit-gateway-attachment-id</code> - The ID of the Connect attachment.</p> </li> <li> <p> <code>transit-gateway-id</code> - The ID of the transit gateway.</p> </li> <li> <p> <code>transport-transit-gateway-attachment-id</code> - The ID of the transit gateway attachment from which the Connect attachment was created.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_max_results.TransitGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
