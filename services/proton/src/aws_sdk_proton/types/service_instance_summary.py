"""Generated from Smithy shape ``com.amazonaws.proton#ServiceInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_proton.types.deployment_id
    import aws_sdk_proton.types.deployment_status
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.service_instance_arn
    import aws_sdk_proton.types.status_message
    import aws_sdk_proton.types.template_version_part


class ServiceInstanceSummary(TypedDict, closed=True):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance.</p>"""
    arn: "aws_sdk_proton.types.service_instance_arn.ServiceInstanceArn"
    """<p>The Amazon Resource Name (ARN) of the service instance.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the service instance was created.</p>"""
    last_deployment_attempted_at: "datetime.datetime"
    """<p>The time when a deployment of the service was last attempted.</p>"""
    last_deployment_succeeded_at: "datetime.datetime"
    """<p>The time when the service was last deployed successfully.</p>"""
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service that the service instance belongs to.</p>"""
    environment_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the environment that the service instance was deployed into.</p>"""
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    template_major_version: (
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The service instance template major version.</p>"""
    template_minor_version: (
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The service instance template minor version.</p>"""
    deployment_status: "aws_sdk_proton.types.deployment_status.DeploymentStatus"
    """<p>The service instance deployment status.</p>"""
    deployment_status_message: NotRequired[
        "aws_sdk_proton.types.status_message.StatusMessage"
    ]
    """<p>A service instance deployment status message.</p>"""
    last_attempted_deployment_id: NotRequired[
        "aws_sdk_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last attempted deployment of this service instance.</p>"""
    last_succeeded_deployment_id: NotRequired[
        "aws_sdk_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last successful deployment of this service instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceInstanceSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import aws_sdk_proton.types._prelude.timestamp

    out["createdAt"] = aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import aws_sdk_proton.types._prelude.timestamp

    out["lastDeploymentAttemptedAt"] = (
        aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_deployment_attempted_at"]
        )
    )
    import aws_sdk_proton.types._prelude.timestamp

    out["lastDeploymentSucceededAt"] = (
        aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_deployment_succeeded_at"]
        )
    )
    out["serviceName"] = value["service_name"]
    out["environmentName"] = value["environment_name"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    out["templateMinorVersion"] = value["template_minor_version"]
    out["deploymentStatus"] = value["deployment_status"]
    if "deployment_status_message" in value:
        out["deploymentStatusMessage"] = value["deployment_status_message"]
    if "last_attempted_deployment_id" in value:
        out["lastAttemptedDeploymentId"] = value["last_attempted_deployment_id"]
    if "last_succeeded_deployment_id" in value:
        out["lastSucceededDeploymentId"] = value["last_succeeded_deployment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceInstanceSummary:
    out: ServiceInstanceSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceInstanceSummary.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ServiceInstanceSummary.arn required")
    if "createdAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ServiceInstanceSummary.created_at required")
    if "lastDeploymentAttemptedAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["last_deployment_attempted_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastDeploymentAttemptedAt"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceInstanceSummary.last_deployment_attempted_at required"
        )
    if "lastDeploymentSucceededAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["last_deployment_succeeded_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastDeploymentSucceededAt"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceInstanceSummary.last_deployment_succeeded_at required"
        )
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("ServiceInstanceSummary.service_name required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("ServiceInstanceSummary.environment_name required")
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("ServiceInstanceSummary.template_name required")
    if "templateMajorVersion" in data:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        raise DeserializationError(
            "ServiceInstanceSummary.template_major_version required"
        )
    if "templateMinorVersion" in data:
        out["template_minor_version"] = data["templateMinorVersion"]
    else:
        raise DeserializationError(
            "ServiceInstanceSummary.template_minor_version required"
        )
    if "deploymentStatus" in data:
        out["deployment_status"] = data["deploymentStatus"]
    else:
        raise DeserializationError("ServiceInstanceSummary.deployment_status required")
    if "deploymentStatusMessage" in data:
        out["deployment_status_message"] = data["deploymentStatusMessage"]
    if "lastAttemptedDeploymentId" in data:
        out["last_attempted_deployment_id"] = data["lastAttemptedDeploymentId"]
    if "lastSucceededDeploymentId" in data:
        out["last_succeeded_deployment_id"] = data["lastSucceededDeploymentId"]
    return out
