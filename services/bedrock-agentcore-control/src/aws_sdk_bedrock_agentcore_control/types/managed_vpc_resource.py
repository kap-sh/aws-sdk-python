"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ManagedVpcResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.endpoint_ip_address_type
    import aws_sdk_bedrock_agentcore_control.types.routing_domain
    import aws_sdk_bedrock_agentcore_control.types.security_group_ids
    import aws_sdk_bedrock_agentcore_control.types.subnet_ids
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.vpc_identifier


class ManagedVpcResource(TypedDict, closed=True):
    vpc_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.vpc_identifier.VpcIdentifier"
    )
    """<p>The ID of the VPC that contains your private resource.</p>"""
    subnet_ids: "aws_sdk_bedrock_agentcore_control.types.subnet_ids.SubnetIds"
    """<p>The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.</p>"""
    endpoint_ip_address_type: "aws_sdk_bedrock_agentcore_control.types.endpoint_ip_address_type.EndpointIpAddressType"
    """<p>The IP address type for the resource configuration endpoint.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>Tags to apply to the managed VPC Lattice resource gateway.</p>"""
    routing_domain: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.routing_domain.RoutingDomain"
    ]
    """<p>An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain[Route traffic through an intermediate domain].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedVpcResource) -> dict:
    out: dict = {}
    out["vpcIdentifier"] = value["vpc_identifier"]
    import aws_sdk_bedrock_agentcore_control.types.subnet_ids

    out["subnetIds"] = (
        aws_sdk_bedrock_agentcore_control.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.endpoint_ip_address_type

    out["endpointIpAddressType"] = (
        aws_sdk_bedrock_agentcore_control.types.endpoint_ip_address_type.serialize_json(
            value["endpoint_ip_address_type"]
        )
    )
    if "security_group_ids" in value:
        import aws_sdk_bedrock_agentcore_control.types.security_group_ids

        out["securityGroupIds"] = (
            aws_sdk_bedrock_agentcore_control.types.security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    if "routing_domain" in value:
        out["routingDomain"] = value["routing_domain"]
    return out


def deserialize_json(data: dict) -> ManagedVpcResource:
    out: ManagedVpcResource = {}  # type: ignore[typeddict-item]
    if "vpcIdentifier" in data:
        out["vpc_identifier"] = data["vpcIdentifier"]
    else:
        raise DeserializationError("ManagedVpcResource.vpc_identifier required")
    if "subnetIds" in data:
        import aws_sdk_bedrock_agentcore_control.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_bedrock_agentcore_control.types.subnet_ids.deserialize_json(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("ManagedVpcResource.subnet_ids required")
    if "endpointIpAddressType" in data:
        import aws_sdk_bedrock_agentcore_control.types.endpoint_ip_address_type

        out["endpoint_ip_address_type"] = (
            aws_sdk_bedrock_agentcore_control.types.endpoint_ip_address_type.deserialize_json(
                data["endpointIpAddressType"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedVpcResource.endpoint_ip_address_type required"
        )
    if "securityGroupIds" in data:
        import aws_sdk_bedrock_agentcore_control.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_bedrock_agentcore_control.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    if "routingDomain" in data:
        out["routing_domain"] = data["routingDomain"]
    return out
