"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetResourceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.domain_name
    import aws_sdk_vpc_lattice.types.domain_verification_arn
    import aws_sdk_vpc_lattice.types.domain_verification_id
    import aws_sdk_vpc_lattice.types.port_range_list
    import aws_sdk_vpc_lattice.types.protocol_type
    import aws_sdk_vpc_lattice.types.resource_configuration_arn
    import aws_sdk_vpc_lattice.types.resource_configuration_definition
    import aws_sdk_vpc_lattice.types.resource_configuration_id
    import aws_sdk_vpc_lattice.types.resource_configuration_name
    import aws_sdk_vpc_lattice.types.resource_configuration_status
    import aws_sdk_vpc_lattice.types.resource_configuration_type
    import aws_sdk_vpc_lattice.types.resource_gateway_id
    import aws_sdk_vpc_lattice.types.timestamp
    import aws_sdk_vpc_lattice.types.verification_status


class GetResourceConfigurationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the resource configuration.</p>"""
    name: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName"
    ]
    """<p>The name of the resource configuration.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource configuration.</p>"""
    resource_gateway_id: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_id.ResourceGatewayId"
    ]
    """<p>The ID of the resource gateway used to connect to the resource configuration in a given VPC. You can specify the resource gateway identifier only for resource configurations with type SINGLE, GROUP, or ARN.</p>"""
    resource_configuration_group_id: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the group resource configuration.</p>"""
    type: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType"
    ]
    """<p>The type of resource configuration.</p> <ul> <li> <p> <code>SINGLE</code> - A single resource.</p> </li> <li> <p> <code>GROUP</code> - A group of resources.</p> </li> <li> <p> <code>CHILD</code> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <code>ARN</code> - An Amazon Web Services resource.</p> </li> </ul>"""
    allow_association_to_shareable_service_network: NotRequired[
        "aws_sdk_vpc_lattice.types.boolean.Boolean"
    ]
    """<p>Specifies whether the resource configuration is associated with a sharable service network.</p>"""
    port_ranges: NotRequired["aws_sdk_vpc_lattice.types.port_range_list.PortRangeList"]
    """<p>The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30</p>"""
    protocol: NotRequired["aws_sdk_vpc_lattice.types.protocol_type.ProtocolType"]
    """<p>The TCP protocol accepted by the specified resource configuration.</p>"""
    custom_domain_name: NotRequired["aws_sdk_vpc_lattice.types.domain_name.DomainName"]
    """<p>The custom domain name of the resource configuration.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_status.ResourceConfigurationStatus"
    ]
    """<p>The status of the resource configuration.</p>"""
    resource_configuration_definition: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
    ]
    """<p>The resource configuration.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the resource configuration was created, in ISO-8601 format.</p>"""
    amazon_managed: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether the resource configuration was created and is managed by Amazon.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason the create-resource-configuration request failed.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The most recent date and time that the resource configuration was updated, in ISO-8601 format.</p>"""
    domain_verification_id: NotRequired[
        "aws_sdk_vpc_lattice.types.domain_verification_id.DomainVerificationId"
    ]
    """<p> The domain verification ID. </p>"""
    domain_verification_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.domain_verification_arn.DomainVerificationArn"
    ]
    """<p> The ARN of the domain verification. </p>"""
    domain_verification_status: NotRequired[
        "aws_sdk_vpc_lattice.types.verification_status.VerificationStatus"
    ]
    """<p> The domain verification status. </p>"""
    group_domain: NotRequired["aws_sdk_vpc_lattice.types.domain_name.DomainName"]
    """<p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceConfigurationResponse) -> dict:
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
        import aws_sdk_vpc_lattice.types.resource_configuration_type

        out["type"] = (
            aws_sdk_vpc_lattice.types.resource_configuration_type.serialize_json(
                value["type"]
            )
        )
    if "allow_association_to_shareable_service_network" in value:
        out["allowAssociationToShareableServiceNetwork"] = value[
            "allow_association_to_shareable_service_network"
        ]
    if "port_ranges" in value:
        import aws_sdk_vpc_lattice.types.port_range_list

        out["portRanges"] = aws_sdk_vpc_lattice.types.port_range_list.serialize_json(
            value["port_ranges"]
        )
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "resource_configuration_definition" in value:
        import aws_sdk_vpc_lattice.types.resource_configuration_definition

        out["resourceConfigurationDefinition"] = (
            aws_sdk_vpc_lattice.types.resource_configuration_definition.serialize_json(
                value["resource_configuration_definition"]
            )
        )
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "amazon_managed" in value:
        out["amazonManaged"] = value["amazon_managed"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "domain_verification_id" in value:
        out["domainVerificationId"] = value["domain_verification_id"]
    if "domain_verification_arn" in value:
        out["domainVerificationArn"] = value["domain_verification_arn"]
    if "domain_verification_status" in value:
        out["domainVerificationStatus"] = value["domain_verification_status"]
    if "group_domain" in value:
        out["groupDomain"] = value["group_domain"]
    return out


def deserialize_json(data: dict) -> GetResourceConfigurationResponse:
    out: GetResourceConfigurationResponse = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_vpc_lattice.types.resource_configuration_type

        out["type"] = (
            aws_sdk_vpc_lattice.types.resource_configuration_type.deserialize_json(
                data["type"]
            )
        )
    if "allowAssociationToShareableServiceNetwork" in data:
        out["allow_association_to_shareable_service_network"] = data[
            "allowAssociationToShareableServiceNetwork"
        ]
    if "portRanges" in data:
        import aws_sdk_vpc_lattice.types.port_range_list

        out["port_ranges"] = aws_sdk_vpc_lattice.types.port_range_list.deserialize_json(
            data["portRanges"]
        )
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "status" in data:
        out["status"] = data["status"]
    if "resourceConfigurationDefinition" in data:
        import aws_sdk_vpc_lattice.types.resource_configuration_definition

        out["resource_configuration_definition"] = (
            aws_sdk_vpc_lattice.types.resource_configuration_definition.deserialize_json(
                data["resourceConfigurationDefinition"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "amazonManaged" in data:
        out["amazon_managed"] = data["amazonManaged"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "domainVerificationId" in data:
        out["domain_verification_id"] = data["domainVerificationId"]
    if "domainVerificationArn" in data:
        out["domain_verification_arn"] = data["domainVerificationArn"]
    if "domainVerificationStatus" in data:
        out["domain_verification_status"] = data["domainVerificationStatus"]
    if "groupDomain" in data:
        out["group_domain"] = data["groupDomain"]
    return out
