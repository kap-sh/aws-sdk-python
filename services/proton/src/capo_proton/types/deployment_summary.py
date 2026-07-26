"""Generated from Smithy shape ``com.amazonaws.proton#DeploymentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.arn
    import capo_proton.types.deployment_arn
    import capo_proton.types.deployment_id
    import capo_proton.types.deployment_status
    import capo_proton.types.deployment_target_resource_type
    import capo_proton.types.resource_name


class DeploymentSummary(TypedDict, closed=True):
    id: "capo_proton.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment.</p>"""
    arn: "capo_proton.types.deployment_arn.DeploymentArn"
    """<p>The Amazon Resource Name (ARN) of the deployment.</p>"""
    target_arn: "capo_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the target of the deployment.</p>"""
    target_resource_created_at: "datetime.datetime"
    """<p>The date and time the target resource was created.</p>"""
    target_resource_type: (
        "capo_proton.types.deployment_target_resource_type.DeploymentTargetResourceType"
    )
    """<p>The resource type of the deployment target. It can be an environment, service, service instance, or component.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the deployment was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The date and time the deployment was last modified.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The date and time the deployment was completed.</p>"""
    environment_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment associated with the deployment.</p>"""
    service_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service associated with the deployment.</p>"""
    service_instance_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service instance associated with the deployment.</p>"""
    component_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the component associated with the deployment.</p>"""
    last_attempted_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last attempted deployment.</p>"""
    last_succeeded_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last successful deployment.</p>"""
    deployment_status: "capo_proton.types.deployment_status.DeploymentStatus"
    """<p>The current status of the deployment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeploymentSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["targetArn"] = value["target_arn"]
    import capo_proton.types._prelude.timestamp

    out["targetResourceCreatedAt"] = (
        capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["target_resource_created_at"]
        )
    )
    out["targetResourceType"] = value["target_resource_type"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    if "completed_at" in value:
        import capo_proton.types._prelude.timestamp

        out["completedAt"] = (
            capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completed_at"]
            )
        )
    out["environmentName"] = value["environment_name"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "last_attempted_deployment_id" in value:
        out["lastAttemptedDeploymentId"] = value["last_attempted_deployment_id"]
    if "last_succeeded_deployment_id" in value:
        out["lastSucceededDeploymentId"] = value["last_succeeded_deployment_id"]
    out["deploymentStatus"] = value["deployment_status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeploymentSummary:
    out: DeploymentSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeploymentSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeploymentSummary.arn required")
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("DeploymentSummary.target_arn required")
    if "targetResourceCreatedAt" in data:
        import capo_proton.types._prelude.timestamp

        out["target_resource_created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["targetResourceCreatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "DeploymentSummary.target_resource_created_at required"
        )
    if "targetResourceType" in data:
        out["target_resource_type"] = data["targetResourceType"]
    else:
        raise DeserializationError("DeploymentSummary.target_resource_type required")
    if "createdAt" in data:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DeploymentSummary.created_at required")
    if "lastModifiedAt" in data:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError("DeploymentSummary.last_modified_at required")
    if "completedAt" in data:
        import capo_proton.types._prelude.timestamp

        out["completed_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["completedAt"]
            )
        )
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("DeploymentSummary.environment_name required")
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "lastAttemptedDeploymentId" in data:
        out["last_attempted_deployment_id"] = data["lastAttemptedDeploymentId"]
    if "lastSucceededDeploymentId" in data:
        out["last_succeeded_deployment_id"] = data["lastSucceededDeploymentId"]
    if "deploymentStatus" in data:
        out["deployment_status"] = data["deploymentStatus"]
    else:
        raise DeserializationError("DeploymentSummary.deployment_status required")
    return out
