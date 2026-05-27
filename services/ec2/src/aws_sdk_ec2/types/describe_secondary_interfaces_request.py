"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondaryInterfacesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_secondary_interfaces_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.secondary_interface_id_list
    import aws_sdk_ec2.types.string


class DescribeSecondaryInterfacesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>attachment.attachment-id</code> - The ID of the secondary interface attachment.</p> </li> <li> <p> <code>attachment.instance-id</code> - The ID of the instance to which the secondary interface is attached.</p> </li> <li> <p> <code>attachment.instance-owner-id</code> - The ID of the Amazon Web Services account that owns the instance to which the secondary interface is attached.</p> </li> <li> <p> <code>attachment.status</code> - The attachment status (<code>attaching</code> | <code>attached</code> | <code>detaching</code> | <code>detached</code>).</p> </li> <li> <p> <code>private-ipv4-addresses.private-ip-address</code> - The private IPv4 address associated with the secondary interface.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the secondary interface.</p> </li> <li> <p> <code>secondary-interface-arn</code> - The ARN of the secondary interface.</p> </li> <li> <p> <code>secondary-interface-id</code> - The ID of the secondary interface.</p> </li> <li> <p> <code>secondary-interface-type</code> - The type of secondary interface (<code>secondary</code>).</p> </li> <li> <p> <code>secondary-network-id</code> - The ID of the secondary network.</p> </li> <li> <p> <code>secondary-network-type</code> - The type of the secondary network (<code>rdma</code>).</p> </li> <li> <p> <code>secondary-subnet-id</code> - The ID of the secondary subnet.</p> </li> <li> <p> <code>status</code> - The status of the secondary interface (<code>available</code> | <code>in-use</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_secondary_interfaces_max_results.DescribeSecondaryInterfacesMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    secondary_interface_ids: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_id_list.SecondaryInterfaceIdList"
    ]
    """<p>The IDs of the secondary interfaces.</p>"""
