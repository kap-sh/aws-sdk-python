"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#DeploymentModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.deployment_status
    import capo_sagemaker_edge.types.entity_name
    import capo_sagemaker_edge.types.model_name
    import capo_sagemaker_edge.types.model_state
    import capo_sagemaker_edge.types.string
    import capo_sagemaker_edge.types.version


class DeploymentModel(TypedDict, closed=True):
    model_handle: NotRequired["capo_sagemaker_edge.types.entity_name.EntityName"]
    """<p>The unique handle of the model.</p>"""
    model_name: NotRequired["capo_sagemaker_edge.types.model_name.ModelName"]
    """<p>The name of the model.</p>"""
    model_version: NotRequired["capo_sagemaker_edge.types.version.Version"]
    """<p>The version of the model.</p>"""
    desired_state: NotRequired["capo_sagemaker_edge.types.model_state.ModelState"]
    """<p>The desired state of the model.</p>"""
    state: NotRequired["capo_sagemaker_edge.types.model_state.ModelState"]
    """<p>Returns the current state of the model.</p>"""
    status: NotRequired["capo_sagemaker_edge.types.deployment_status.DeploymentStatus"]
    """<p>Returns the deployment status of the model.</p>"""
    status_reason: NotRequired["capo_sagemaker_edge.types.string.String"]
    """<p>Returns the error message for the deployment status result.</p>"""
    rollback_failure_reason: NotRequired["capo_sagemaker_edge.types.string.String"]
    """<p>Returns the error message if there is a rollback.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentModel) -> dict:
    out: dict = {}
    if "model_handle" in value:
        out["ModelHandle"] = value["model_handle"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "desired_state" in value:
        import capo_sagemaker_edge.types.model_state

        out["DesiredState"] = capo_sagemaker_edge.types.model_state.serialize_json(
            value["desired_state"]
        )
    if "state" in value:
        import capo_sagemaker_edge.types.model_state

        out["State"] = capo_sagemaker_edge.types.model_state.serialize_json(
            value["state"]
        )
    if "status" in value:
        import capo_sagemaker_edge.types.deployment_status

        out["Status"] = capo_sagemaker_edge.types.deployment_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "rollback_failure_reason" in value:
        out["RollbackFailureReason"] = value["rollback_failure_reason"]
    return out


def deserialize_json(data: dict) -> DeploymentModel:
    out: DeploymentModel = {}  # type: ignore[typeddict-item]
    if "ModelHandle" in data:
        out["model_handle"] = data["ModelHandle"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "DesiredState" in data:
        import capo_sagemaker_edge.types.model_state

        out["desired_state"] = capo_sagemaker_edge.types.model_state.deserialize_json(
            data["DesiredState"]
        )
    if "State" in data:
        import capo_sagemaker_edge.types.model_state

        out["state"] = capo_sagemaker_edge.types.model_state.deserialize_json(
            data["State"]
        )
    if "Status" in data:
        import capo_sagemaker_edge.types.deployment_status

        out["status"] = capo_sagemaker_edge.types.deployment_status.deserialize_json(
            data["Status"]
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "RollbackFailureReason" in data:
        out["rollback_failure_reason"] = data["RollbackFailureReason"]
    return out
