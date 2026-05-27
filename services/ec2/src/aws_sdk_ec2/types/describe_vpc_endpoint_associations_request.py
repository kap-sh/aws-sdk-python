"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.max_results2
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint_id_list


class DescribeVpcEndpointAssociationsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_endpoint_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_id_list.VpcEndpointIdList"
    ]
    """<p>The IDs of the VPC endpoints.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>vpc-endpoint-id</code> - The ID of the VPC endpoint.</p> </li> <li> <p> <code>associated-resource-accessibility</code> - The association state. When the state is <code>accessible</code>, it returns <code>AVAILABLE</code>. When the state is <code>inaccessible</code>, it returns <code>PENDING</code> or <code>FAILED</code>.</p> </li> <li> <p> <code>association-id</code> - The ID of the VPC endpoint association.</p> </li> <li> <p> <code>associated-resource-id</code> - The ID of the associated resource configuration.</p> </li> <li> <p> <code>service-network-arn</code> - The Amazon Resource Name (ARN) of the associated service network. Only VPC endpoints of type service network will be returned.</p> </li> <li> <p> <code>resource-configuration-group-arn</code> - The Amazon Resource Name (ARN) of the resource configuration of type GROUP.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.max_results2.MaxResults2"]
    """<p>The maximum page size.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The pagination token.</p>"""
