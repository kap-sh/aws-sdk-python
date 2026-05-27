"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressesAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_attribute_name
    import aws_sdk_ec2.types.address_max_results
    import aws_sdk_ec2.types.allocation_ids
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.next_token


class DescribeAddressesAttributeRequest(TypedDict):
    allocation_ids: NotRequired["aws_sdk_ec2.types.allocation_ids.AllocationIds"]
    """<p>[EC2-VPC] The allocation IDs.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.address_attribute_name.AddressAttributeName"
    ]
    """<p>The attribute of the IP address.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.address_max_results.AddressMaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
