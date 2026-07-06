"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpcEndpointServiceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_list
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsEc2VpcEndpointServiceDetails(TypedDict, closed=True):
    acceptance_required: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether requests from other Amazon Web Services accounts to create an endpoint to the service must first be accepted.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The Availability Zones where the service is available.</p>"""
    base_endpoint_dns_names: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The DNS names for the service.</p>"""
    manages_vpc_endpoints: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the service manages its VPC endpoints.</p>"""
    gateway_load_balancer_arns: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The ARNs of the Gateway Load Balancers for the service.</p>"""
    network_load_balancer_arns: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The ARNs of the Network Load Balancers for the service.</p>"""
    private_dns_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The private DNS name for the service.</p>"""
    service_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the service.</p>"""
    service_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the service.</p>"""
    service_state: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The current state of the service. Valid values are as follows:</p> <ul> <li> <p> <code>Available</code> </p> </li> <li> <p> <code>Deleted</code> </p> </li> <li> <p> <code>Deleting</code> </p> </li> <li> <p> <code>Failed</code> </p> </li> <li> <p> <code>Pending</code> </p> </li> </ul>"""
    service_type: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_list.AwsEc2VpcEndpointServiceServiceTypeList"
    ]
    """<p>The types for the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpcEndpointServiceDetails) -> dict:
    out: dict = {}
    if "acceptance_required" in value:
        out["AcceptanceRequired"] = value["acceptance_required"]
    if "availability_zones" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["AvailabilityZones"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["availability_zones"]
            )
        )
    if "base_endpoint_dns_names" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["BaseEndpointDnsNames"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["base_endpoint_dns_names"]
            )
        )
    if "manages_vpc_endpoints" in value:
        out["ManagesVpcEndpoints"] = value["manages_vpc_endpoints"]
    if "gateway_load_balancer_arns" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["GatewayLoadBalancerArns"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["gateway_load_balancer_arns"]
            )
        )
    if "network_load_balancer_arns" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["NetworkLoadBalancerArns"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["network_load_balancer_arns"]
            )
        )
    if "private_dns_name" in value:
        out["PrivateDnsName"] = value["private_dns_name"]
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "service_state" in value:
        out["ServiceState"] = value["service_state"]
    if "service_type" in value:
        import aws_sdk_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_list

        out["ServiceType"] = (
            aws_sdk_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_list.serialize_json(
                value["service_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2VpcEndpointServiceDetails:
    out: AwsEc2VpcEndpointServiceDetails = {}  # type: ignore[typeddict-item]
    if "AcceptanceRequired" in data:
        out["acceptance_required"] = data["AcceptanceRequired"]
    if "AvailabilityZones" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["availability_zones"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    if "BaseEndpointDnsNames" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["base_endpoint_dns_names"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["BaseEndpointDnsNames"]
            )
        )
    if "ManagesVpcEndpoints" in data:
        out["manages_vpc_endpoints"] = data["ManagesVpcEndpoints"]
    if "GatewayLoadBalancerArns" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["gateway_load_balancer_arns"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["GatewayLoadBalancerArns"]
            )
        )
    if "NetworkLoadBalancerArns" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["network_load_balancer_arns"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["NetworkLoadBalancerArns"]
            )
        )
    if "PrivateDnsName" in data:
        out["private_dns_name"] = data["PrivateDnsName"]
    if "ServiceId" in data:
        out["service_id"] = data["ServiceId"]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "ServiceState" in data:
        out["service_state"] = data["ServiceState"]
    if "ServiceType" in data:
        import aws_sdk_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_list

        out["service_type"] = (
            aws_sdk_securityhub.types.aws_ec2_vpc_endpoint_service_service_type_list.deserialize_json(
                data["ServiceType"]
            )
        )
    return out
