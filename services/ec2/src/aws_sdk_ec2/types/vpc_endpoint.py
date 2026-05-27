"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dns_entry_set
    import aws_sdk_ec2.types.dns_options
    import aws_sdk_ec2.types.group_identifier_set
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.last_error
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.resource_configuration_arn
    import aws_sdk_ec2.types.service_network_arn
    import aws_sdk_ec2.types.state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_ip_prefixes_list
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.vpc_endpoint_type


class VpcEndpoint(TypedDict):
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the endpoint.</p>"""
    vpc_endpoint_type: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_type.VpcEndpointType"
    ]
    """<p>The type of endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC to which the endpoint is associated.</p>"""
    service_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the service to which the endpoint is associated.</p>"""
    state: NotRequired["aws_sdk_ec2.types.state.State"]
    """<p>The state of the endpoint.</p>"""
    policy_document: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The policy document associated with the endpoint, if applicable.</p>"""
    route_table_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>(Gateway endpoint) The IDs of the route tables associated with the endpoint.</p>"""
    subnet_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>(Interface endpoint) The subnets for the endpoint.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_identifier_set.GroupIdentifierSet"]
    """<p>(Interface endpoint) Information about the security groups that are associated with the network interface.</p>"""
    ip_address_type: NotRequired["aws_sdk_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the endpoint.</p>"""
    dns_options: NotRequired["aws_sdk_ec2.types.dns_options.DnsOptions"]
    """<p>The DNS options for the endpoint.</p>"""
    private_dns_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>(Interface endpoint) Indicates whether the VPC is associated with a private hosted zone.</p>"""
    requester_managed: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the endpoint is being managed by its service.</p>"""
    network_interface_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>(Interface endpoint) The network interfaces for the endpoint.</p>"""
    dns_entries: NotRequired["aws_sdk_ec2.types.dns_entry_set.DnsEntrySet"]
    """<p>(Interface endpoint) The DNS entries for the endpoint.</p>"""
    creation_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time that the endpoint was created.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the endpoint.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the endpoint.</p>"""
    last_error: NotRequired["aws_sdk_ec2.types.last_error.LastError"]
    """<p>The last error that occurred for endpoint.</p>"""
    ipv4_prefixes: NotRequired[
        "aws_sdk_ec2.types.subnet_ip_prefixes_list.SubnetIpPrefixesList"
    ]
    """<p>Array of IPv4 prefixes.</p>"""
    ipv6_prefixes: NotRequired[
        "aws_sdk_ec2.types.subnet_ip_prefixes_list.SubnetIpPrefixesList"
    ]
    """<p>Array of IPv6 prefixes.</p>"""
    failure_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reason for the failure.</p>"""
    service_network_arn: NotRequired[
        "aws_sdk_ec2.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    resource_configuration_arn: NotRequired[
        "aws_sdk_ec2.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource configuration.</p>"""
    service_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region where the service is hosted.</p>"""
