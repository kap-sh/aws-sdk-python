"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.domain_name
    import capo_vpc_lattice.types.domain_verification_id
    import capo_vpc_lattice.types.resource_configuration_arn
    import capo_vpc_lattice.types.resource_configuration_id
    import capo_vpc_lattice.types.resource_configuration_name
    import capo_vpc_lattice.types.resource_configuration_status
    import capo_vpc_lattice.types.resource_configuration_type
    import capo_vpc_lattice.types.resource_gateway_id
    import capo_vpc_lattice.types.timestamp


class ResourceConfigurationSummary(TypedDict, closed=True):
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
    """<p>The ID of the resource gateway.</p>"""
    resource_configuration_group_id: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the group resource configuration.</p>"""
    type: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType"
    ]
    """<p>The type of resource configuration.</p> <ul> <li> <p> <code>SINGLE</code> - A single resource.</p> </li> <li> <p> <code>GROUP</code> - A group of resources. You must create a group resource configuration before you create a child resource configuration.</p> </li> <li> <p> <code>CHILD</code> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <code>ARN</code> - An Amazon Web Services resource.</p> </li> </ul>"""
    status: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_status.ResourceConfigurationStatus"
    ]
    """<p>The status of the resource configuration.</p>"""
    amazon_managed: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether the resource configuration was created and is managed by Amazon.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the resource configuration was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The most recent date and time that the resource configuration was updated, in ISO-8601 format.</p>"""
    custom_domain_name: NotRequired["capo_vpc_lattice.types.domain_name.DomainName"]
    """<p> The custom domain name. </p>"""
    domain_verification_id: NotRequired[
        "capo_vpc_lattice.types.domain_verification_id.DomainVerificationId"
    ]
    """<p> The domain verification ID. </p>"""
    group_domain: NotRequired["capo_vpc_lattice.types.domain_name.DomainName"]
    """<p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigurationSummary) -> dict:
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
    if "status" in value:
        out["status"] = value["status"]
    if "amazon_managed" in value:
        out["amazonManaged"] = value["amazon_managed"]
    if "created_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "domain_verification_id" in value:
        out["domainVerificationId"] = value["domain_verification_id"]
    if "group_domain" in value:
        out["groupDomain"] = value["group_domain"]
    return out


def deserialize_json(data: dict) -> ResourceConfigurationSummary:
    out: ResourceConfigurationSummary = {}  # type: ignore[typeddict-item]
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
    if "status" in data:
        out["status"] = data["status"]
    if "amazonManaged" in data:
        out["amazon_managed"] = data["amazonManaged"]
    if "createdAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "domainVerificationId" in data:
        out["domain_verification_id"] = data["domainVerificationId"]
    if "groupDomain" in data:
        out["group_domain"] = data["groupDomain"]
    return out
