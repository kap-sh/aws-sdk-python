"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceEndpointAssociationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.account_id
    import aws_sdk_vpc_lattice.types.resource_configuration_arn
    import aws_sdk_vpc_lattice.types.resource_configuration_id
    import aws_sdk_vpc_lattice.types.resource_configuration_name
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_arn
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_id
    import aws_sdk_vpc_lattice.types.timestamp
    import aws_sdk_vpc_lattice.types.vpc_endpoint_id
    import aws_sdk_vpc_lattice.types.vpc_endpoint_owner


class ResourceEndpointAssociationSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_endpoint_association_id.ResourceEndpointAssociationId"
    ]
    """<p>The ID of the VPC endpoint association.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_endpoint_association_arn.ResourceEndpointAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the VPC endpoint association.</p>"""
    resource_configuration_id: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the resource configuration.</p>"""
    resource_configuration_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource configuration.</p>"""
    resource_configuration_name: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName"
    ]
    """<p>The name of the resource configuration.</p>"""
    vpc_endpoint_id: NotRequired[
        "aws_sdk_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the VPC endpoint.</p>"""
    vpc_endpoint_owner: NotRequired[
        "aws_sdk_vpc_lattice.types.vpc_endpoint_owner.VpcEndpointOwner"
    ]
    """<p>The owner of the VPC endpoint.</p>"""
    created_by: NotRequired["aws_sdk_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the VPC endpoint association was created, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceEndpointAssociationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "resource_configuration_id" in value:
        out["resourceConfigurationId"] = value["resource_configuration_id"]
    if "resource_configuration_arn" in value:
        out["resourceConfigurationArn"] = value["resource_configuration_arn"]
    if "resource_configuration_name" in value:
        out["resourceConfigurationName"] = value["resource_configuration_name"]
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_endpoint_owner" in value:
        out["vpcEndpointOwner"] = value["vpc_endpoint_owner"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> ResourceEndpointAssociationSummary:
    out: ResourceEndpointAssociationSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "resourceConfigurationId" in data:
        out["resource_configuration_id"] = data["resourceConfigurationId"]
    if "resourceConfigurationArn" in data:
        out["resource_configuration_arn"] = data["resourceConfigurationArn"]
    if "resourceConfigurationName" in data:
        out["resource_configuration_name"] = data["resourceConfigurationName"]
    if "vpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    if "vpcEndpointOwner" in data:
        out["vpc_endpoint_owner"] = data["vpcEndpointOwner"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    return out
