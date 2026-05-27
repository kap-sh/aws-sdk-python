"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dns_name_state
    import aws_sdk_ec2.types.payer_responsibility
    import aws_sdk_ec2.types.private_dns_details_set
    import aws_sdk_ec2.types.service_type_detail_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.supported_ip_address_types
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list


class ServiceDetail(TypedDict):
    service_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the service.</p>"""
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the endpoint service.</p>"""
    service_type: NotRequired[
        "aws_sdk_ec2.types.service_type_detail_set.ServiceTypeDetailSet"
    ]
    """<p>The type of service.</p>"""
    service_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region where the service is hosted.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the service owner.</p>"""
    base_endpoint_dns_names: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The DNS names for the service.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private DNS name for the service.</p>"""
    private_dns_names: NotRequired[
        "aws_sdk_ec2.types.private_dns_details_set.PrivateDnsDetailsSet"
    ]
    """<p>The private DNS names assigned to the VPC endpoint service.</p>"""
    vpc_endpoint_policy_supported: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the service supports endpoint policies.</p>"""
    acceptance_required: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether VPC endpoint connection requests to the service must be accepted by the service owner.</p>"""
    manages_vpc_endpoints: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.</p>"""
    payer_responsibility: NotRequired[
        "aws_sdk_ec2.types.payer_responsibility.PayerResponsibility"
    ]
    """<p>The payer responsibility.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the service.</p>"""
    private_dns_name_verification_state: NotRequired[
        "aws_sdk_ec2.types.dns_name_state.DnsNameState"
    ]
    """<p>The verification state of the VPC endpoint service.</p> <p>Consumers of the endpoint service cannot use the private name when the state is not <code>verified</code>.</p>"""
    supported_ip_address_types: NotRequired[
        "aws_sdk_ec2.types.supported_ip_address_types.SupportedIpAddressTypes"
    ]
    """<p>The supported IP address types.</p>"""
