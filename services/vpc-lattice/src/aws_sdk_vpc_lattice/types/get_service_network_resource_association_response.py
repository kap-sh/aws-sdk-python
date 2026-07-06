"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceNetworkResourceAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.account_id
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.dns_entry
    import aws_sdk_vpc_lattice.types.resource_configuration_arn
    import aws_sdk_vpc_lattice.types.resource_configuration_id
    import aws_sdk_vpc_lattice.types.resource_configuration_name
    import aws_sdk_vpc_lattice.types.service_network_identifier_without_regex
    import aws_sdk_vpc_lattice.types.service_network_name_without_regex
    import aws_sdk_vpc_lattice.types.service_network_resource_association_arn
    import aws_sdk_vpc_lattice.types.service_network_resource_association_id
    import aws_sdk_vpc_lattice.types.service_network_resource_association_status
    import aws_sdk_vpc_lattice.types.timestamp
    import aws_sdk_vpc_lattice.types.verification_status


class GetServiceNetworkResourceAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_resource_association_id.ServiceNetworkResourceAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_resource_association_arn.ServiceNetworkResourceAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_resource_association_status.ServiceNetworkResourceAssociationStatus"
    ]
    """<p>The status of the association.</p>"""
    created_by: NotRequired["aws_sdk_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the association was created, in ISO-8601 format.</p>"""
    resource_configuration_id: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the resource configuration that is associated with the service network.</p>"""
    resource_configuration_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    resource_configuration_name: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName"
    ]
    """<p>The name of the resource configuration that is associated with the service network.</p>"""
    service_network_id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex"
    ]
    """<p>The ID of the service network that is associated with the resource configuration.</p>"""
    service_network_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network that is associated with the resource configuration.</p>"""
    service_network_name: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_name_without_regex.ServiceNetworkNameWithoutRegex"
    ]
    """<p>The name of the service network that is associated with the resource configuration.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason the association request failed.</p>"""
    failure_code: NotRequired["str"]
    """<p>The failure code.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The most recent date and time that the association was updated, in ISO-8601 format.</p>"""
    private_dns_entry: NotRequired["aws_sdk_vpc_lattice.types.dns_entry.DnsEntry"]
    """<p>The private DNS entry for the service.</p>"""
    private_dns_enabled: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled in the service network resource association. </p>"""
    dns_entry: NotRequired["aws_sdk_vpc_lattice.types.dns_entry.DnsEntry"]
    """<p>The DNS entry for the service.</p>"""
    is_managed_association: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether the association is managed by Amazon.</p>"""
    domain_verification_status: NotRequired[
        "aws_sdk_vpc_lattice.types.verification_status.VerificationStatus"
    ]
    """<p> The domain verification status in the service network resource association. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceNetworkResourceAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "resource_configuration_id" in value:
        out["resourceConfigurationId"] = value["resource_configuration_id"]
    if "resource_configuration_arn" in value:
        out["resourceConfigurationArn"] = value["resource_configuration_arn"]
    if "resource_configuration_name" in value:
        out["resourceConfigurationName"] = value["resource_configuration_name"]
    if "service_network_id" in value:
        out["serviceNetworkId"] = value["service_network_id"]
    if "service_network_arn" in value:
        out["serviceNetworkArn"] = value["service_network_arn"]
    if "service_network_name" in value:
        out["serviceNetworkName"] = value["service_network_name"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "private_dns_entry" in value:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["privateDnsEntry"] = aws_sdk_vpc_lattice.types.dns_entry.serialize_json(
            value["private_dns_entry"]
        )
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "dns_entry" in value:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dnsEntry"] = aws_sdk_vpc_lattice.types.dns_entry.serialize_json(
            value["dns_entry"]
        )
    if "is_managed_association" in value:
        out["isManagedAssociation"] = value["is_managed_association"]
    if "domain_verification_status" in value:
        out["domainVerificationStatus"] = value["domain_verification_status"]
    return out


def deserialize_json(data: dict) -> GetServiceNetworkResourceAssociationResponse:
    out: GetServiceNetworkResourceAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "resourceConfigurationId" in data:
        out["resource_configuration_id"] = data["resourceConfigurationId"]
    if "resourceConfigurationArn" in data:
        out["resource_configuration_arn"] = data["resourceConfigurationArn"]
    if "resourceConfigurationName" in data:
        out["resource_configuration_name"] = data["resourceConfigurationName"]
    if "serviceNetworkId" in data:
        out["service_network_id"] = data["serviceNetworkId"]
    if "serviceNetworkArn" in data:
        out["service_network_arn"] = data["serviceNetworkArn"]
    if "serviceNetworkName" in data:
        out["service_network_name"] = data["serviceNetworkName"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "privateDnsEntry" in data:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["private_dns_entry"] = aws_sdk_vpc_lattice.types.dns_entry.deserialize_json(
            data["privateDnsEntry"]
        )
    if "privateDnsEnabled" in data:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if "dnsEntry" in data:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dns_entry"] = aws_sdk_vpc_lattice.types.dns_entry.deserialize_json(
            data["dnsEntry"]
        )
    if "isManagedAssociation" in data:
        out["is_managed_association"] = data["isManagedAssociation"]
    if "domainVerificationStatus" in data:
        out["domain_verification_status"] = data["domainVerificationStatus"]
    return out
