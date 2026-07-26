"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#DeploymentModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.deployment_model

DeploymentModels: TypeAlias = list[
    "capo_sagemaker_edge.types.deployment_model.DeploymentModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentModels) -> list:
    import capo_sagemaker_edge.types.deployment_model

    out: list = []
    for item in value:
        out.append(capo_sagemaker_edge.types.deployment_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeploymentModels:
    import capo_sagemaker_edge.types.deployment_model

    out: DeploymentModels = []
    for item in data:
        out.append(capo_sagemaker_edge.types.deployment_model.deserialize_json(item))
    return out
