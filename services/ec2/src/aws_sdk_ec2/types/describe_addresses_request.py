"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.public_ip_string_list


class DescribeAddressesRequest(TypedDict):
    public_ips: NotRequired[
        "aws_sdk_ec2.types.public_ip_string_list.PublicIpStringList"
    ]
    """<p>One or more Elastic IP addresses.</p> <p>Default: Describes all your Elastic IP addresses.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p> <ul> <li> <p> <code>allocation-id</code> - The allocation ID for the address.</p> </li> <li> <p> <code>association-id</code> - The association ID for the address.</p> </li> <li> <p> <code>instance-id</code> - The ID of the instance the address is associated with, if any.</p> </li> <li> <p> <code>network-border-group</code> - A unique set of Availability Zones, Local Zones, or Wavelength Zones from where Amazon Web Services advertises IP addresses. </p> </li> <li> <p> <code>network-interface-id</code> - The ID of the network interface that the address is associated with, if any.</p> </li> <li> <p> <code>network-interface-owner-id</code> - The Amazon Web Services account ID of the owner.</p> </li> <li> <p> <code>private-ip-address</code> - The private IP address associated with the Elastic IP address.</p> </li> <li> <p> <code>public-ip</code> - The Elastic IP address, or the carrier IP address.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    allocation_ids: NotRequired["aws_sdk_ec2.types.allocation_id_list.AllocationIdList"]
    """<p>Information about the allocation IDs.</p>"""
