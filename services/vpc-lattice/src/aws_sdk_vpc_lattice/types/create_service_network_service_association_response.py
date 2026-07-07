"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkServiceAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.account_id
    import aws_sdk_vpc_lattice.types.dns_entry
    import aws_sdk_vpc_lattice.types.service_custom_domain_name
    import aws_sdk_vpc_lattice.types.service_network_service_association_arn
    import aws_sdk_vpc_lattice.types.service_network_service_association_identifier
    import aws_sdk_vpc_lattice.types.service_network_service_association_status


class CreateServiceNetworkServiceAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier"
    ]
    """<p>The ID of the association.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_status.ServiceNetworkServiceAssociationStatus"
    ]
    """<p>The association status.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_arn.ServiceNetworkServiceAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    created_by: NotRequired["aws_sdk_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    custom_domain_name: NotRequired[
        "aws_sdk_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
    ]
    """<p>The custom domain name of the service.</p>"""
    dns_entry: NotRequired["aws_sdk_vpc_lattice.types.dns_entry.DnsEntry"]
    """<p>The DNS name of the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkServiceAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "dns_entry" in value:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dnsEntry"] = aws_sdk_vpc_lattice.types.dns_entry.serialize_json(
            value["dns_entry"]
        )
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkServiceAssociationResponse:
    out: CreateServiceNetworkServiceAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "dnsEntry" in data:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dns_entry"] = aws_sdk_vpc_lattice.types.dns_entry.deserialize_json(
            data["dnsEntry"]
        )
    return out
