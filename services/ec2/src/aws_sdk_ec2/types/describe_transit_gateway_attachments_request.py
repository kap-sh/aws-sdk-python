"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayAttachmentsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id_string_list
    import aws_sdk_ec2.types.transit_gateway_max_results


class DescribeTransitGatewayAttachmentsRequest(TypedDict):
    transit_gateway_attachment_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id_string_list.TransitGatewayAttachmentIdStringList"
    ]
    """<p>The IDs of the attachments.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>association.state</code> - The state of the association (<code>associating</code> | <code>associated</code> | <code>disassociating</code>).</p> </li> <li> <p> <code>association.transit-gateway-route-table-id</code> - The ID of the route table for the transit gateway.</p> </li> <li> <p> <code>resource-id</code> - The ID of the resource.</p> </li> <li> <p> <code>resource-owner-id</code> - The ID of the Amazon Web Services account that owns the resource.</p> </li> <li> <p> <code>resource-type</code> - The resource type. Valid values are <code>vpc</code> | <code>vpn</code> | <code>direct-connect-gateway</code> | <code>peering</code> | <code>connect</code>.</p> </li> <li> <p> <code>state</code> - The state of the attachment. Valid values are <code>available</code> | <code>deleted</code> | <code>deleting</code> | <code>failed</code> | <code>failing</code> | <code>initiatingRequest</code> | <code>modifying</code> | <code>pendingAcceptance</code> | <code>pending</code> | <code>rollingBack</code> | <code>rejected</code> | <code>rejecting</code>.</p> </li> <li> <p> <code>transit-gateway-attachment-id</code> - The ID of the attachment.</p> </li> <li> <p> <code>transit-gateway-id</code> - The ID of the transit gateway.</p> </li> <li> <p> <code>transit-gateway-owner-id</code> - The ID of the Amazon Web Services account that owns the transit gateway.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_max_results.TransitGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
