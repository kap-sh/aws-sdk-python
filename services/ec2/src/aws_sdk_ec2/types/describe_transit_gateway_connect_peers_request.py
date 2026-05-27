"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayConnectPeersRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_connect_peer_id_string_list
    import aws_sdk_ec2.types.transit_gateway_max_results


class DescribeTransitGatewayConnectPeersRequest(TypedDict):
    transit_gateway_connect_peer_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer_id_string_list.TransitGatewayConnectPeerIdStringList"
    ]
    """<p>The IDs of the Connect peers.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>state</code> - The state of the Connect peer (<code>pending</code> | <code>available</code> | <code>deleting</code> | <code>deleted</code>).</p> </li> <li> <p> <code>transit-gateway-attachment-id</code> - The ID of the attachment.</p> </li> <li> <p> <code>transit-gateway-connect-peer-id</code> - The ID of the Connect peer.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_max_results.TransitGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
