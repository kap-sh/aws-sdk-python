"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#EdgeDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.definitions
    import capo_sagemaker_edge.types.deployment_type
    import capo_sagemaker_edge.types.entity_name
    import capo_sagemaker_edge.types.failure_handling_policy


class EdgeDeployment(TypedDict, closed=True):
    deployment_name: NotRequired["capo_sagemaker_edge.types.entity_name.EntityName"]
    """<p>The name and unique ID of the deployment.</p>"""
    type: NotRequired["capo_sagemaker_edge.types.deployment_type.DeploymentType"]
    """<p>The type of the deployment.</p>"""
    failure_handling_policy: NotRequired[
        "capo_sagemaker_edge.types.failure_handling_policy.FailureHandlingPolicy"
    ]
    """<p>Determines whether to rollback to previous configuration if deployment fails.</p>"""
    definitions: NotRequired["capo_sagemaker_edge.types.definitions.Definitions"]
    """<p>Returns a list of Definition objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EdgeDeployment) -> dict:
    out: dict = {}
    if "deployment_name" in value:
        out["DeploymentName"] = value["deployment_name"]
    if "type" in value:
        import capo_sagemaker_edge.types.deployment_type

        out["Type"] = capo_sagemaker_edge.types.deployment_type.serialize_json(
            value["type"]
        )
    if "failure_handling_policy" in value:
        import capo_sagemaker_edge.types.failure_handling_policy

        out["FailureHandlingPolicy"] = (
            capo_sagemaker_edge.types.failure_handling_policy.serialize_json(
                value["failure_handling_policy"]
            )
        )
    if "definitions" in value:
        import capo_sagemaker_edge.types.definitions

        out["Definitions"] = capo_sagemaker_edge.types.definitions.serialize_json(
            value["definitions"]
        )
    return out


def deserialize_json(data: dict) -> EdgeDeployment:
    out: EdgeDeployment = {}  # type: ignore[typeddict-item]
    if "DeploymentName" in data:
        out["deployment_name"] = data["DeploymentName"]
    if "Type" in data:
        import capo_sagemaker_edge.types.deployment_type

        out["type"] = capo_sagemaker_edge.types.deployment_type.deserialize_json(
            data["Type"]
        )
    if "FailureHandlingPolicy" in data:
        import capo_sagemaker_edge.types.failure_handling_policy

        out["failure_handling_policy"] = (
            capo_sagemaker_edge.types.failure_handling_policy.deserialize_json(
                data["FailureHandlingPolicy"]
            )
        )
    if "Definitions" in data:
        import capo_sagemaker_edge.types.definitions

        out["definitions"] = capo_sagemaker_edge.types.definitions.deserialize_json(
            data["Definitions"]
        )
    return out
