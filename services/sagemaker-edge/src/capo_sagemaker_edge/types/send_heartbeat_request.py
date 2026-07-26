"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#SendHeartbeatRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.deployment_result
    import capo_sagemaker_edge.types.device_fleet_name
    import capo_sagemaker_edge.types.device_name
    import capo_sagemaker_edge.types.edge_metrics
    import capo_sagemaker_edge.types.models
    import capo_sagemaker_edge.types.version


class SendHeartbeatRequest(TypedDict, closed=True):
    agent_metrics: NotRequired["capo_sagemaker_edge.types.edge_metrics.EdgeMetrics"]
    """<p>For internal use. Returns a list of SageMaker Edge Manager agent operating metrics.</p>"""
    models: NotRequired["capo_sagemaker_edge.types.models.Models"]
    """<p>Returns a list of models deployed on the the device.</p>"""
    agent_version: NotRequired["capo_sagemaker_edge.types.version.Version"]
    """<p>Returns the version of the agent.</p>"""
    device_name: NotRequired["capo_sagemaker_edge.types.device_name.DeviceName"]
    """<p>The unique name of the device.</p>"""
    device_fleet_name: NotRequired[
        "capo_sagemaker_edge.types.device_fleet_name.DeviceFleetName"
    ]
    """<p>The name of the fleet that the device belongs to.</p>"""
    deployment_result: NotRequired[
        "capo_sagemaker_edge.types.deployment_result.DeploymentResult"
    ]
    """<p>Returns the result of a deployment on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendHeartbeatRequest) -> dict:
    out: dict = {}
    if "agent_metrics" in value:
        import capo_sagemaker_edge.types.edge_metrics

        out["AgentMetrics"] = capo_sagemaker_edge.types.edge_metrics.serialize_json(
            value["agent_metrics"]
        )
    if "models" in value:
        import capo_sagemaker_edge.types.models

        out["Models"] = capo_sagemaker_edge.types.models.serialize_json(value["models"])
    if "agent_version" in value:
        out["AgentVersion"] = value["agent_version"]
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "deployment_result" in value:
        import capo_sagemaker_edge.types.deployment_result

        out["DeploymentResult"] = (
            capo_sagemaker_edge.types.deployment_result.serialize_json(
                value["deployment_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendHeartbeatRequest:
    out: SendHeartbeatRequest = {}  # type: ignore[typeddict-item]
    if "AgentMetrics" in data:
        import capo_sagemaker_edge.types.edge_metrics

        out["agent_metrics"] = capo_sagemaker_edge.types.edge_metrics.deserialize_json(
            data["AgentMetrics"]
        )
    if "Models" in data:
        import capo_sagemaker_edge.types.models

        out["models"] = capo_sagemaker_edge.types.models.deserialize_json(
            data["Models"]
        )
    if "AgentVersion" in data:
        out["agent_version"] = data["AgentVersion"]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "DeploymentResult" in data:
        import capo_sagemaker_edge.types.deployment_result

        out["deployment_result"] = (
            capo_sagemaker_edge.types.deployment_result.deserialize_json(
                data["DeploymentResult"]
            )
        )
    return out
