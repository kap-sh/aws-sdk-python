"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.payer_responsibility
    import aws_sdk_ec2.types.private_dns_name_configuration
    import aws_sdk_ec2.types.service_state
    import aws_sdk_ec2.types.service_type_detail_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.supported_ip_address_types
    import aws_sdk_ec2.types.supported_region_set
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list


class ServiceConfiguration(TypedDict):
    service_type: NotRequired[
        "aws_sdk_ec2.types.service_type_detail_set.ServiceTypeDetailSet"
    ]
    """<p>The type of service.</p>"""
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service.</p>"""
    service_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the service.</p>"""
    service_state: NotRequired["aws_sdk_ec2.types.service_state.ServiceState"]
    """<p>The service state.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    acceptance_required: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether requests from other Amazon Web Services accounts to create an endpoint to the service must first be accepted.</p>"""
    manages_vpc_endpoints: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.</p>"""
    network_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Network Load Balancers for the service.</p>"""
    gateway_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service.</p>"""
    supported_ip_address_types: NotRequired[
        "aws_sdk_ec2.types.supported_ip_address_types.SupportedIpAddressTypes"
    ]
    """<p>The supported IP address types.</p>"""
    base_endpoint_dns_names: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The DNS names for the service.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private DNS name for the service.</p>"""
    private_dns_name_configuration: NotRequired[
        "aws_sdk_ec2.types.private_dns_name_configuration.PrivateDnsNameConfiguration"
    ]
    """<p>Information about the endpoint service private DNS name configuration.</p>"""
    payer_responsibility: NotRequired[
        "aws_sdk_ec2.types.payer_responsibility.PayerResponsibility"
    ]
    """<p>The payer responsibility.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the service.</p>"""
    supported_regions: NotRequired[
        "aws_sdk_ec2.types.supported_region_set.SupportedRegionSet"
    ]
    """<p>The supported Regions.</p>"""
    remote_access_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether consumers can access the service from a Region other than the Region where the service is hosted.</p>"""
