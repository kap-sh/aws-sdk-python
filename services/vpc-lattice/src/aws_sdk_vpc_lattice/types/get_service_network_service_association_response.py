"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceNetworkServiceAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.account_id
    import aws_sdk_vpc_lattice.types.dns_entry
    import aws_sdk_vpc_lattice.types.service_arn
    import aws_sdk_vpc_lattice.types.service_custom_domain_name
    import aws_sdk_vpc_lattice.types.service_id
    import aws_sdk_vpc_lattice.types.service_name
    import aws_sdk_vpc_lattice.types.service_network_arn
    import aws_sdk_vpc_lattice.types.service_network_id
    import aws_sdk_vpc_lattice.types.service_network_name
    import aws_sdk_vpc_lattice.types.service_network_service_association_arn
    import aws_sdk_vpc_lattice.types.service_network_service_association_identifier
    import aws_sdk_vpc_lattice.types.service_network_service_association_status
    import aws_sdk_vpc_lattice.types.timestamp


class GetServiceNetworkServiceAssociationResponse(TypedDict):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier"
    ]
    """<p>The ID of the service network and service association.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_status.ServiceNetworkServiceAssociationStatus"
    ]
    """<p>The status of the association.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_arn.ServiceNetworkServiceAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    created_by: NotRequired["aws_sdk_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the association was created, in ISO-8601 format.</p>"""
    service_id: NotRequired["aws_sdk_vpc_lattice.types.service_id.ServiceId"]
    """<p>The ID of the service.</p>"""
    service_name: NotRequired["aws_sdk_vpc_lattice.types.service_name.ServiceName"]
    """<p>The name of the service.</p>"""
    service_arn: NotRequired["aws_sdk_vpc_lattice.types.service_arn.ServiceArn"]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    service_network_id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_id.ServiceNetworkId"
    ]
    """<p>The ID of the service network.</p>"""
    service_network_name: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_name.ServiceNetworkName"
    ]
    """<p>The name of the service network.</p>"""
    service_network_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    dns_entry: NotRequired["aws_sdk_vpc_lattice.types.dns_entry.DnsEntry"]
    """<p>The DNS name of the service.</p>"""
    custom_domain_name: NotRequired[
        "aws_sdk_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
    ]
    """<p>The custom domain name of the service.</p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message.</p>"""
    failure_code: NotRequired["str"]
    """<p>The failure code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceNetworkServiceAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "service_id" in value:
        out["serviceId"] = value["service_id"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "service_network_id" in value:
        out["serviceNetworkId"] = value["service_network_id"]
    if "service_network_name" in value:
        out["serviceNetworkName"] = value["service_network_name"]
    if "service_network_arn" in value:
        out["serviceNetworkArn"] = value["service_network_arn"]
    if "dns_entry" in value:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dnsEntry"] = aws_sdk_vpc_lattice.types.dns_entry.serialize_json(
            value["dns_entry"]
        )
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_json(data: dict) -> GetServiceNetworkServiceAssociationResponse:
    out: GetServiceNetworkServiceAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "serviceId" in data:
        out["service_id"] = data["serviceId"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "serviceNetworkId" in data:
        out["service_network_id"] = data["serviceNetworkId"]
    if "serviceNetworkName" in data:
        out["service_network_name"] = data["serviceNetworkName"]
    if "serviceNetworkArn" in data:
        out["service_network_arn"] = data["serviceNetworkArn"]
    if "dnsEntry" in data:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dns_entry"] = aws_sdk_vpc_lattice.types.dns_entry.deserialize_json(
            data["dnsEntry"]
        )
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    return out
