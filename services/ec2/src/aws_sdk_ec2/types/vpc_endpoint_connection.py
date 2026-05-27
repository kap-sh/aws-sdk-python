"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointConnection``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dns_entry_set
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list


class VpcEndpointConnection(TypedDict):
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service to which the endpoint is connected.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint.</p>"""
    vpc_endpoint_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the VPC endpoint.</p>"""
    vpc_endpoint_state: NotRequired["aws_sdk_ec2.types.state.State"]
    """<p>The state of the VPC endpoint.</p>"""
    creation_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time that the VPC endpoint was created.</p>"""
    dns_entries: NotRequired["aws_sdk_ec2.types.dns_entry_set.DnsEntrySet"]
    """<p>The DNS entries for the VPC endpoint.</p>"""
    network_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the network load balancers for the service.</p>"""
    gateway_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service.</p>"""
    ip_address_type: NotRequired["aws_sdk_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the endpoint.</p>"""
    vpc_endpoint_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint connection.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    vpc_endpoint_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region of the endpoint.</p>"""
