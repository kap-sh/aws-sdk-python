"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceNetworkVpcAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.account_id
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.dns_options
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.service_network_arn
    import capo_vpc_lattice.types.service_network_id
    import capo_vpc_lattice.types.service_network_name
    import capo_vpc_lattice.types.service_network_vpc_association_arn
    import capo_vpc_lattice.types.service_network_vpc_association_id
    import capo_vpc_lattice.types.service_network_vpc_association_status
    import capo_vpc_lattice.types.timestamp
    import capo_vpc_lattice.types.vpc_id


class GetServiceNetworkVpcAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_id.ServiceNetworkVpcAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_status.ServiceNetworkVpcAssociationStatus"
    ]
    """<p>The status of the association.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_arn.ServiceNetworkVpcAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    created_by: NotRequired["capo_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the association was created, in ISO-8601 format.</p>"""
    service_network_id: NotRequired[
        "capo_vpc_lattice.types.service_network_id.ServiceNetworkId"
    ]
    """<p>The ID of the service network.</p>"""
    service_network_name: NotRequired[
        "capo_vpc_lattice.types.service_network_name.ServiceNetworkName"
    ]
    """<p>The name of the service network.</p>"""
    service_network_arn: NotRequired[
        "capo_vpc_lattice.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    vpc_id: NotRequired["capo_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    security_group_ids: NotRequired[
        "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups.</p>"""
    private_dns_enabled: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled in the VPC association. </p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message.</p>"""
    failure_code: NotRequired["str"]
    """<p>The failure code.</p>"""
    last_updated_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the association was last updated, in ISO-8601 format.</p>"""
    dns_options: NotRequired["capo_vpc_lattice.types.dns_options.DnsOptions"]
    """<p> DNS options for the service network VPC association. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceNetworkVpcAssociationResponse) -> dict:
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
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "service_network_id" in value:
        out["serviceNetworkId"] = value["service_network_id"]
    if "service_network_name" in value:
        out["serviceNetworkName"] = value["service_network_name"]
    if "service_network_arn" in value:
        out["serviceNetworkArn"] = value["service_network_arn"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "security_group_ids" in value:
        import capo_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            capo_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "last_updated_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "dns_options" in value:
        import capo_vpc_lattice.types.dns_options

        out["dnsOptions"] = capo_vpc_lattice.types.dns_options.serialize_json(
            value["dns_options"]
        )
    return out


def deserialize_json(data: dict) -> GetServiceNetworkVpcAssociationResponse:
    out: GetServiceNetworkVpcAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "serviceNetworkId" in data:
        out["service_network_id"] = data["serviceNetworkId"]
    if "serviceNetworkName" in data:
        out["service_network_name"] = data["serviceNetworkName"]
    if "serviceNetworkArn" in data:
        out["service_network_arn"] = data["serviceNetworkArn"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "securityGroupIds" in data:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "privateDnsEnabled" in data:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "lastUpdatedAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "dnsOptions" in data:
        import capo_vpc_lattice.types.dns_options

        out["dns_options"] = capo_vpc_lattice.types.dns_options.deserialize_json(
            data["dnsOptions"]
        )
    return out
