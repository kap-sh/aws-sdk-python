"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkEndpointAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_arn
    import aws_sdk_vpc_lattice.types.timestamp


class ServiceNetworkEndpointAssociation(TypedDict):
    vpc_endpoint_id: NotRequired["str"]
    """<p>The ID of the VPC endpoint associated with the service network.</p>"""
    vpc_id: NotRequired["str"]
    """<p>The ID of the VPC for the association.</p>"""
    vpc_endpoint_owner_id: NotRequired["str"]
    """<p>The owner of the VPC endpoint associated with the service network.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the association.</p>"""
    state: NotRequired["str"]
    """<p>The state of the association.</p>"""
    service_network_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the association was created, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkEndpointAssociation) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "vpc_endpoint_owner_id" in value:
        out["vpcEndpointOwnerId"] = value["vpc_endpoint_owner_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "state" in value:
        out["state"] = value["state"]
    if "service_network_arn" in value:
        out["serviceNetworkArn"] = value["service_network_arn"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> ServiceNetworkEndpointAssociation:
    out: ServiceNetworkEndpointAssociation = {}  # type: ignore[typeddict-item]
    if "vpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "vpcEndpointOwnerId" in data:
        out["vpc_endpoint_owner_id"] = data["vpcEndpointOwnerId"]
    if "id" in data:
        out["id"] = data["id"]
    if "state" in data:
        out["state"] = data["state"]
    if "serviceNetworkArn" in data:
        out["service_network_arn"] = data["serviceNetworkArn"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    return out
