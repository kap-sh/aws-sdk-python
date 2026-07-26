"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateResourceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.domain_name
    import capo_vpc_lattice.types.domain_verification_arn
    import capo_vpc_lattice.types.domain_verification_id
    import capo_vpc_lattice.types.port_range_list
    import capo_vpc_lattice.types.protocol_type
    import capo_vpc_lattice.types.resource_configuration_arn
    import capo_vpc_lattice.types.resource_configuration_definition
    import capo_vpc_lattice.types.resource_configuration_id
    import capo_vpc_lattice.types.resource_configuration_name
    import capo_vpc_lattice.types.resource_configuration_status
    import capo_vpc_lattice.types.resource_configuration_type
    import capo_vpc_lattice.types.resource_gateway_id
    import capo_vpc_lattice.types.timestamp


class CreateResourceConfigurationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the resource configuration.</p>"""
    name: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName"
    ]
    """<p>The name of the resource configuration.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource configuration.</p>"""
    resource_gateway_id: NotRequired[
        "capo_vpc_lattice.types.resource_gateway_id.ResourceGatewayId"
    ]
    """<p>The ID of the resource gateway associated with the resource configuration.</p>"""
    resource_configuration_group_id: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the parent resource configuration of type <code>GROUP</code>.</p>"""
    type: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType"
    ]
    """<p>The type of resource configuration. A resource configuration can be one of the following types:</p> <ul> <li> <p> <b>SINGLE</b> - A single resource.</p> </li> <li> <p> <b>GROUP</b> - A group of resources. You must create a group resource configuration before you create a child resource configuration.</p> </li> <li> <p> <b>CHILD</b> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <b>ARN</b> - An Amazon Web Services resource.</p> </li> </ul>"""
    port_ranges: NotRequired["capo_vpc_lattice.types.port_range_list.PortRangeList"]
    """<p>The port range.</p>"""
    protocol: NotRequired["capo_vpc_lattice.types.protocol_type.ProtocolType"]
    """<p>The protocol.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_status.ResourceConfigurationStatus"
    ]
    """<p>The current status of the resource configuration.</p>"""
    resource_configuration_definition: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
    ]
    """<p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>"""
    allow_association_to_shareable_service_network: NotRequired[
        "capo_vpc_lattice.types.boolean.Boolean"
    ]
    """<p>Specifies whether the resource configuration can be associated with a sharable service network.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the resource configuration was created, in ISO-8601 format.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason that the request failed.</p>"""
    custom_domain_name: NotRequired["capo_vpc_lattice.types.domain_name.DomainName"]
    """<p> The custom domain name for your resource configuration. </p>"""
    domain_verification_id: NotRequired[
        "capo_vpc_lattice.types.domain_verification_id.DomainVerificationId"
    ]
    """<p> The domain name verification ID. </p>"""
    group_domain: NotRequired["capo_vpc_lattice.types.domain_name.DomainName"]
    """<p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>"""
    domain_verification_arn: NotRequired[
        "capo_vpc_lattice.types.domain_verification_arn.DomainVerificationArn"
    ]
    """<p> The verification ID ARN </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceConfigurationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "resource_gateway_id" in value:
        out["resourceGatewayId"] = value["resource_gateway_id"]
    if "resource_configuration_group_id" in value:
        out["resourceConfigurationGroupId"] = value["resource_configuration_group_id"]
    if "type" in value:
        import capo_vpc_lattice.types.resource_configuration_type

        out["type"] = capo_vpc_lattice.types.resource_configuration_type.serialize_json(
            value["type"]
        )
    if "port_ranges" in value:
        import capo_vpc_lattice.types.port_range_list

        out["portRanges"] = capo_vpc_lattice.types.port_range_list.serialize_json(
            value["port_ranges"]
        )
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "status" in value:
        out["status"] = value["status"]
    if "resource_configuration_definition" in value:
        import capo_vpc_lattice.types.resource_configuration_definition

        out["resourceConfigurationDefinition"] = (
            capo_vpc_lattice.types.resource_configuration_definition.serialize_json(
                value["resource_configuration_definition"]
            )
        )
    if "allow_association_to_shareable_service_network" in value:
        out["allowAssociationToShareableServiceNetwork"] = value[
            "allow_association_to_shareable_service_network"
        ]
    if "created_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "domain_verification_id" in value:
        out["domainVerificationId"] = value["domain_verification_id"]
    if "group_domain" in value:
        out["groupDomain"] = value["group_domain"]
    if "domain_verification_arn" in value:
        out["domainVerificationArn"] = value["domain_verification_arn"]
    return out


def deserialize_json(data: dict) -> CreateResourceConfigurationResponse:
    out: CreateResourceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "resourceGatewayId" in data:
        out["resource_gateway_id"] = data["resourceGatewayId"]
    if "resourceConfigurationGroupId" in data:
        out["resource_configuration_group_id"] = data["resourceConfigurationGroupId"]
    if "type" in data:
        import capo_vpc_lattice.types.resource_configuration_type

        out["type"] = (
            capo_vpc_lattice.types.resource_configuration_type.deserialize_json(
                data["type"]
            )
        )
    if "portRanges" in data:
        import capo_vpc_lattice.types.port_range_list

        out["port_ranges"] = capo_vpc_lattice.types.port_range_list.deserialize_json(
            data["portRanges"]
        )
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "status" in data:
        out["status"] = data["status"]
    if "resourceConfigurationDefinition" in data:
        import capo_vpc_lattice.types.resource_configuration_definition

        out["resource_configuration_definition"] = (
            capo_vpc_lattice.types.resource_configuration_definition.deserialize_json(
                data["resourceConfigurationDefinition"]
            )
        )
    if "allowAssociationToShareableServiceNetwork" in data:
        out["allow_association_to_shareable_service_network"] = data[
            "allowAssociationToShareableServiceNetwork"
        ]
    if "createdAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "domainVerificationId" in data:
        out["domain_verification_id"] = data["domainVerificationId"]
    if "groupDomain" in data:
        out["group_domain"] = data["groupDomain"]
    if "domainVerificationArn" in data:
        out["domain_verification_arn"] = data["domainVerificationArn"]
    return out
