"""Generated from Smithy shape ``com.amazonaws.datazone#Deployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.deployment_messages_list
    import aws_sdk_datazone.types.deployment_status
    import aws_sdk_datazone.types.deployment_type
    import aws_sdk_datazone.types.environment_error


class Deployment(TypedDict, closed=True):
    deployment_id: NotRequired["str"]
    """<p>The identifier of the last deployment of the environment.</p>"""
    deployment_type: NotRequired[
        "aws_sdk_datazone.types.deployment_type.DeploymentType"
    ]
    """<p>The type of the last deployment of the environment.</p>"""
    deployment_status: NotRequired[
        "aws_sdk_datazone.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the last deployment of the environment.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_datazone.types.environment_error.EnvironmentError"
    ]
    """<p>The failure reason of the last deployment of the environment.</p>"""
    messages: NotRequired[
        "aws_sdk_datazone.types.deployment_messages_list.DeploymentMessagesList"
    ]
    """<p>The messages of the last deployment of the environment.</p>"""
    is_deployment_complete: NotRequired["bool"]
    """<p>Specifies whether the last deployment of the environment is complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Deployment) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "deployment_type" in value:
        import aws_sdk_datazone.types.deployment_type

        out["deploymentType"] = aws_sdk_datazone.types.deployment_type.serialize_json(
            value["deployment_type"]
        )
    if "deployment_status" in value:
        import aws_sdk_datazone.types.deployment_status

        out["deploymentStatus"] = (
            aws_sdk_datazone.types.deployment_status.serialize_json(
                value["deployment_status"]
            )
        )
    if "failure_reason" in value:
        import aws_sdk_datazone.types.environment_error

        out["failureReason"] = aws_sdk_datazone.types.environment_error.serialize_json(
            value["failure_reason"]
        )
    if "messages" in value:
        import aws_sdk_datazone.types.deployment_messages_list

        out["messages"] = (
            aws_sdk_datazone.types.deployment_messages_list.serialize_json(
                value["messages"]
            )
        )
    if "is_deployment_complete" in value:
        out["isDeploymentComplete"] = value["is_deployment_complete"]
    return out


def deserialize_json(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "deploymentType" in data:
        import aws_sdk_datazone.types.deployment_type

        out["deployment_type"] = (
            aws_sdk_datazone.types.deployment_type.deserialize_json(
                data["deploymentType"]
            )
        )
    if "deploymentStatus" in data:
        import aws_sdk_datazone.types.deployment_status

        out["deployment_status"] = (
            aws_sdk_datazone.types.deployment_status.deserialize_json(
                data["deploymentStatus"]
            )
        )
    if "failureReason" in data:
        import aws_sdk_datazone.types.environment_error

        out["failure_reason"] = (
            aws_sdk_datazone.types.environment_error.deserialize_json(
                data["failureReason"]
            )
        )
    if "messages" in data:
        import aws_sdk_datazone.types.deployment_messages_list

        out["messages"] = (
            aws_sdk_datazone.types.deployment_messages_list.deserialize_json(
                data["messages"]
            )
        )
    if "isDeploymentComplete" in data:
        out["is_deployment_complete"] = data["isDeploymentComplete"]
    return out
