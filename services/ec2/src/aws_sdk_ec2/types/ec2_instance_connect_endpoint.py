"""Generated from Smithy shape ``com.amazonaws.ec2#Ec2InstanceConnectEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ec2_instance_connect_endpoint_state
    import aws_sdk_ec2.types.instance_connect_endpoint_id
    import aws_sdk_ec2.types.instance_connect_endpoint_public_dns_names
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_interface_id_set
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.security_group_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_id


class Ec2InstanceConnectEndpoint(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that created the EC2 Instance Connect Endpoint.</p>"""
    instance_connect_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_id.InstanceConnectEndpointId"
    ]
    """<p>The ID of the EC2 Instance Connect Endpoint.</p>"""
    instance_connect_endpoint_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the EC2 Instance Connect Endpoint.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ec2_instance_connect_endpoint_state.Ec2InstanceConnectEndpointState"
    ]
    """<p>The current state of the EC2 Instance Connect Endpoint.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The message for the current state of the EC2 Instance Connect Endpoint. Can include a failure message.</p>"""
    dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name of the EC2 Instance Connect Endpoint.</p>"""
    fips_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Federal Information Processing Standards (FIPS) compliant DNS name of the EC2 Instance Connect Endpoint.</p>"""
    network_interface_ids: NotRequired[
        "aws_sdk_ec2.types.network_interface_id_set.NetworkInterfaceIdSet"
    ]
    """<p>The ID of the elastic network interface that Amazon EC2 automatically created when creating the EC2 Instance Connect Endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC in which the EC2 Instance Connect Endpoint was created.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the EC2 Instance Connect Endpoint.</p>"""
    created_at: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time that the EC2 Instance Connect Endpoint was created.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which the EC2 Instance Connect Endpoint was created.</p>"""
    preserve_client_ip: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether your client's IP address is preserved as the source when you connect to a resource. The following are the possible values.</p> <ul> <li> <p> <code>true</code> - Use the IP address of the client. Your instance must have an IPv4 address.</p> </li> <li> <p> <code>false</code> - Use the IP address of the network interface.</p> </li> </ul> <p>Default: <code>false</code> </p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_set.SecurityGroupIdSet"
    ]
    """<p>The security groups associated with the endpoint. If you didn't specify a security group, the default security group for your VPC is associated with the endpoint.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the EC2 Instance Connect Endpoint.</p>"""
    ip_address_type: NotRequired["aws_sdk_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type of the endpoint.</p>"""
    public_dns_names: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_public_dns_names.InstanceConnectEndpointPublicDnsNames"
    ]
    """<p>The public DNS names of the endpoint.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the EC2 Instance Connect Endpoint.</p>"""
