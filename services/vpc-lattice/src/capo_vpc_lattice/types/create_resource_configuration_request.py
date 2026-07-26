"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateResourceConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.domain_name
    import capo_vpc_lattice.types.domain_verification_identifier
    import capo_vpc_lattice.types.port_range_list
    import capo_vpc_lattice.types.protocol_type
    import capo_vpc_lattice.types.resource_configuration_definition
    import capo_vpc_lattice.types.resource_configuration_identifier
    import capo_vpc_lattice.types.resource_configuration_name
    import capo_vpc_lattice.types.resource_configuration_type
    import capo_vpc_lattice.types.resource_gateway_identifier
    import capo_vpc_lattice.types.tag_map


class CreateResourceConfigurationRequest(TypedDict, closed=True):
    name: "capo_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName"
    """<p>The name of the resource configuration. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>"""
    type: "capo_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType"
    """<p>The type of resource configuration. A resource configuration can be one of the following types:</p> <ul> <li> <p> <b>SINGLE</b> - A single resource.</p> </li> <li> <p> <b>GROUP</b> - A group of resources. You must create a group resource configuration before you create a child resource configuration.</p> </li> <li> <p> <b>CHILD</b> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <b>ARN</b> - An Amazon Web Services resource.</p> </li> </ul>"""
    port_ranges: NotRequired["capo_vpc_lattice.types.port_range_list.PortRangeList"]
    """<p>(SINGLE, GROUP, CHILD) The TCP port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30).</p>"""
    protocol: NotRequired["capo_vpc_lattice.types.protocol_type.ProtocolType"]
    """<p>(SINGLE, GROUP) The protocol accepted by the resource configuration.</p>"""
    resource_gateway_identifier: NotRequired[
        "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
    ]
    """<p>(SINGLE, GROUP, ARN) The ID or ARN of the resource gateway used to connect to the resource configuration. For a child resource configuration, this value is inherited from the parent resource configuration.</p>"""
    resource_configuration_group_identifier: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    ]
    """<p>(CHILD) The ID or ARN of the parent resource configuration of type <code>GROUP</code>. This is used to associate a child resource configuration with a group resource configuration.</p>"""
    resource_configuration_definition: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
    ]
    """<p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>"""
    allow_association_to_shareable_service_network: NotRequired[
        "capo_vpc_lattice.types.boolean.Boolean"
    ]
    """<p>(SINGLE, GROUP, ARN) Specifies whether the resource configuration can be associated with a sharable service network. The default is false.</p>"""
    custom_domain_name: NotRequired["capo_vpc_lattice.types.domain_name.DomainName"]
    """<p> A custom domain name for your resource configuration. Additionally, provide a DomainVerificationID to prove your ownership of a domain. </p>"""
    group_domain: NotRequired["capo_vpc_lattice.types.domain_name.DomainName"]
    """<p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>"""
    domain_verification_identifier: NotRequired[
        "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
    ]
    """<p> The domain verification ID of your verified custom domain name. If you don't provide an ID, you must configure the DNS settings yourself. </p>"""
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the resource configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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
    if "resource_gateway_identifier" in value:
        out["resourceGatewayIdentifier"] = value["resource_gateway_identifier"]
    if "resource_configuration_group_identifier" in value:
        out["resourceConfigurationGroupIdentifier"] = value[
            "resource_configuration_group_identifier"
        ]
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
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "group_domain" in value:
        out["groupDomain"] = value["group_domain"]
    if "domain_verification_identifier" in value:
        out["domainVerificationIdentifier"] = value["domain_verification_identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateResourceConfigurationRequest:
    out: CreateResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateResourceConfigurationRequest.name required")
    if "type" in data:
        import capo_vpc_lattice.types.resource_configuration_type

        out["type"] = (
            capo_vpc_lattice.types.resource_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("CreateResourceConfigurationRequest.type required")
    if "portRanges" in data:
        import capo_vpc_lattice.types.port_range_list

        out["port_ranges"] = capo_vpc_lattice.types.port_range_list.deserialize_json(
            data["portRanges"]
        )
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "resourceGatewayIdentifier" in data:
        out["resource_gateway_identifier"] = data["resourceGatewayIdentifier"]
    if "resourceConfigurationGroupIdentifier" in data:
        out["resource_configuration_group_identifier"] = data[
            "resourceConfigurationGroupIdentifier"
        ]
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
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "groupDomain" in data:
        out["group_domain"] = data["groupDomain"]
    if "domainVerificationIdentifier" in data:
        out["domain_verification_identifier"] = data["domainVerificationIdentifier"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
