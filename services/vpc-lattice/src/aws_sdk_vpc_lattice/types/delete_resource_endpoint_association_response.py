"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteResourceEndpointAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_configuration_arn
    import aws_sdk_vpc_lattice.types.resource_configuration_id
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_arn
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_id
    import aws_sdk_vpc_lattice.types.vpc_endpoint_id


class DeleteResourceEndpointAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_endpoint_association_id.ResourceEndpointAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_endpoint_association_arn.ResourceEndpointAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    resource_configuration_id: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the resource configuration.</p>"""
    resource_configuration_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource configuration associated with the VPC endpoint of type resource.</p>"""
    vpc_endpoint_id: NotRequired[
        "aws_sdk_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the resource VPC endpoint that is associated with the resource configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceEndpointAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "resource_configuration_id" in value:
        out["resourceConfigurationId"] = value["resource_configuration_id"]
    if "resource_configuration_arn" in value:
        out["resourceConfigurationArn"] = value["resource_configuration_arn"]
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_json(data: dict) -> DeleteResourceEndpointAssociationResponse:
    out: DeleteResourceEndpointAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "resourceConfigurationId" in data:
        out["resource_configuration_id"] = data["resourceConfigurationId"]
    if "resourceConfigurationArn" in data:
        out["resource_configuration_arn"] = data["resourceConfigurationArn"]
    if "vpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    return out
