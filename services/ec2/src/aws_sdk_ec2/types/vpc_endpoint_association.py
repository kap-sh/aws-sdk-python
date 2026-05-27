"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dns_entry
    import aws_sdk_ec2.types.service_network_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_endpoint_id


class VpcEndpointAssociation(TypedDict):
    id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint association.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the VPC endpoint.</p>"""
    service_network_arn: NotRequired[
        "aws_sdk_ec2.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    service_network_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the service network.</p>"""
    associated_resource_accessibility: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The connectivity status of the resources associated to a VPC endpoint. The resource is accessible if the associated resource configuration is <code>AVAILABLE</code>, otherwise the resource is inaccessible.</p>"""
    failure_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message related to why an VPC endpoint association failed.</p>"""
    failure_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An error code related to why an VPC endpoint association failed.</p>"""
    dns_entry: NotRequired["aws_sdk_ec2.types.dns_entry.DnsEntry"]
    """<p>The DNS entry of the VPC endpoint association.</p>"""
    private_dns_entry: NotRequired["aws_sdk_ec2.types.dns_entry.DnsEntry"]
    """<p>The private DNS entry of the VPC endpoint association.</p>"""
    associated_resource_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the associated resource.</p>"""
    resource_configuration_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource configuration group.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags to apply to the VPC endpoint association.</p>"""
