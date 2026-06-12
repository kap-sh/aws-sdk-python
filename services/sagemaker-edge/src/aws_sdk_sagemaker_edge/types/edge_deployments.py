"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#EdgeDeployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_edge.types.edge_deployment

EdgeDeployments: TypeAlias = list[
    "aws_sdk_sagemaker_edge.types.edge_deployment.EdgeDeployment"
]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeDeployments) -> list:
    import aws_sdk_sagemaker_edge.types.edge_deployment

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_edge.types.edge_deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> EdgeDeployments:
    import aws_sdk_sagemaker_edge.types.edge_deployment

    out: EdgeDeployments = []
    for item in data:
        out.append(aws_sdk_sagemaker_edge.types.edge_deployment.deserialize_json(item))
    return out
