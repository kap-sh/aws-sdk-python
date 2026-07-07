"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkVpcAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.account_id
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.dns_options
    import aws_sdk_vpc_lattice.types.service_network_arn
    import aws_sdk_vpc_lattice.types.service_network_id
    import aws_sdk_vpc_lattice.types.service_network_name
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_arn
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_id
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_status
    import aws_sdk_vpc_lattice.types.timestamp
    import aws_sdk_vpc_lattice.types.vpc_id


class ServiceNetworkVpcAssociationSummary(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_vpc_association_id.ServiceNetworkVpcAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_vpc_association_arn.ServiceNetworkVpcAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_vpc_association_status.ServiceNetworkVpcAssociationStatus"
    ]
    """<p>The status.</p>"""
    created_by: NotRequired["aws_sdk_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the association was created, in ISO-8601 format.</p>"""
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
    private_dns_enabled: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled for the service network VPC association. </p>"""
    dns_options: NotRequired["aws_sdk_vpc_lattice.types.dns_options.DnsOptions"]
    """<p> The DNS options for the service network VPC association. </p>"""
    vpc_id: NotRequired["aws_sdk_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the association was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkVpcAssociationSummary) -> dict:
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
    if "service_network_id" in value:
        out["serviceNetworkId"] = value["service_network_id"]
    if "service_network_name" in value:
        out["serviceNetworkName"] = value["service_network_name"]
    if "service_network_arn" in value:
        out["serviceNetworkArn"] = value["service_network_arn"]
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "dns_options" in value:
        import aws_sdk_vpc_lattice.types.dns_options

        out["dnsOptions"] = aws_sdk_vpc_lattice.types.dns_options.serialize_json(
            value["dns_options"]
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ServiceNetworkVpcAssociationSummary:
    out: ServiceNetworkVpcAssociationSummary = {}  # type: ignore[typeddict-item]
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
    if "serviceNetworkId" in data:
        out["service_network_id"] = data["serviceNetworkId"]
    if "serviceNetworkName" in data:
        out["service_network_name"] = data["serviceNetworkName"]
    if "serviceNetworkArn" in data:
        out["service_network_arn"] = data["serviceNetworkArn"]
    if "privateDnsEnabled" in data:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if "dnsOptions" in data:
        import aws_sdk_vpc_lattice.types.dns_options

        out["dns_options"] = aws_sdk_vpc_lattice.types.dns_options.deserialize_json(
            data["dnsOptions"]
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
