"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CreatePrivateGraphEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.security_group_ids
    import aws_sdk_neptune_graph.types.subnet_ids
    import aws_sdk_neptune_graph.types.vpc_id


class CreatePrivateGraphEndpointInput(TypedDict, closed=True):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    vpc_id: NotRequired["aws_sdk_neptune_graph.types.vpc_id.VpcId"]
    """<p> The VPC in which the private graph endpoint needs to be created.</p>"""
    subnet_ids: NotRequired["aws_sdk_neptune_graph.types.subnet_ids.SubnetIds"]
    """<p>Subnets in which private graph endpoint ENIs are created.</p>"""
    vpc_security_group_ids: NotRequired[
        "aws_sdk_neptune_graph.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>Security groups to be attached to the private graph endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivateGraphEndpointInput) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_neptune_graph.types.subnet_ids

        out["subnetIds"] = aws_sdk_neptune_graph.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "vpc_security_group_ids" in value:
        import aws_sdk_neptune_graph.types.security_group_ids

        out["vpcSecurityGroupIds"] = (
            aws_sdk_neptune_graph.types.security_group_ids.serialize_json(
                value["vpc_security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreatePrivateGraphEndpointInput:
    out: CreatePrivateGraphEndpointInput = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "subnetIds" in data:
        import aws_sdk_neptune_graph.types.subnet_ids

        out["subnet_ids"] = aws_sdk_neptune_graph.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    if "vpcSecurityGroupIds" in data:
        import aws_sdk_neptune_graph.types.security_group_ids

        out["vpc_security_group_ids"] = (
            aws_sdk_neptune_graph.types.security_group_ids.deserialize_json(
                data["vpcSecurityGroupIds"]
            )
        )
    return out
