"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CreatePrivateGraphEndpointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.private_graph_endpoint_status
    import aws_sdk_neptune_graph.types.subnet_ids
    import aws_sdk_neptune_graph.types.vpc_endpoint_id
    import aws_sdk_neptune_graph.types.vpc_id


class CreatePrivateGraphEndpointOutput(TypedDict, closed=True):
    vpc_id: "aws_sdk_neptune_graph.types.vpc_id.VpcId"
    """<p>VPC in which the private graph endpoint is created.</p>"""
    subnet_ids: "aws_sdk_neptune_graph.types.subnet_ids.SubnetIds"
    """<p>Subnets in which the private graph endpoint ENIs are created. </p>"""
    status: "aws_sdk_neptune_graph.types.private_graph_endpoint_status.PrivateGraphEndpointStatus"
    """<p>Status of the private graph endpoint.</p>"""
    vpc_endpoint_id: NotRequired[
        "aws_sdk_neptune_graph.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>Endpoint ID of the private graph endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivateGraphEndpointOutput) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import aws_sdk_neptune_graph.types.subnet_ids

    out["subnetIds"] = aws_sdk_neptune_graph.types.subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_neptune_graph.types.private_graph_endpoint_status

    out["status"] = (
        aws_sdk_neptune_graph.types.private_graph_endpoint_status.serialize_json(
            value["status"]
        )
    )
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_json(data: dict) -> CreatePrivateGraphEndpointOutput:
    out: CreatePrivateGraphEndpointOutput = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("CreatePrivateGraphEndpointOutput.vpc_id required")
    if "subnetIds" in data:
        import aws_sdk_neptune_graph.types.subnet_ids

        out["subnet_ids"] = aws_sdk_neptune_graph.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError(
            "CreatePrivateGraphEndpointOutput.subnet_ids required"
        )
    if "status" in data:
        import aws_sdk_neptune_graph.types.private_graph_endpoint_status

        out["status"] = (
            aws_sdk_neptune_graph.types.private_graph_endpoint_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreatePrivateGraphEndpointOutput.status required")
    if "vpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    return out
