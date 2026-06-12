"""Generated from Smithy shape ``com.amazonaws.bedrock#GetCustomModelDeploymentResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_arn
    import aws_sdk_bedrock.types.custom_model_deployment_arn
    import aws_sdk_bedrock.types.custom_model_deployment_description
    import aws_sdk_bedrock.types.custom_model_deployment_status
    import aws_sdk_bedrock.types.custom_model_deployment_update_details
    import aws_sdk_bedrock.types.error_message
    import aws_sdk_bedrock.types.model_deployment_name
    import aws_sdk_bedrock.types.timestamp


class GetCustomModelDeploymentResponse(TypedDict):
    custom_model_deployment_arn: (
        "aws_sdk_bedrock.types.custom_model_deployment_arn.CustomModelDeploymentArn"
    )
    """<p>The Amazon Resource Name (ARN) of the custom model deployment.</p>"""
    model_deployment_name: (
        "aws_sdk_bedrock.types.model_deployment_name.ModelDeploymentName"
    )
    """<p>The name of the custom model deployment.</p>"""
    model_arn: "aws_sdk_bedrock.types.custom_model_arn.CustomModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model associated with this deployment.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The date and time when the custom model deployment was created.</p>"""
    status: "aws_sdk_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
    """<p>The status of the custom model deployment. Possible values are:</p> <ul> <li> <p> <code>CREATING</code> - The deployment is being set up and prepared for inference.</p> </li> <li> <p> <code>ACTIVE</code> - The deployment is ready and available for inference requests.</p> </li> <li> <p> <code>FAILED</code> - The deployment failed to be created or became unavailable.</p> </li> </ul>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.custom_model_deployment_description.CustomModelDeploymentDescription"
    ]
    """<p>The description of the custom model deployment.</p>"""
    update_details: NotRequired[
        "aws_sdk_bedrock.types.custom_model_deployment_update_details.CustomModelDeploymentUpdateDetails"
    ]
    """<p> Details about any pending or completed updates to the custom model deployment, including the new model ARN and update status. </p>"""
    failure_message: NotRequired["aws_sdk_bedrock.types.error_message.ErrorMessage"]
    """<p>If the deployment status is <code>FAILED</code>, this field contains a message describing the failure reason.</p>"""
    last_updated_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The date and time when the custom model deployment was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomModelDeploymentResponse) -> dict:
    out: dict = {}
    out["customModelDeploymentArn"] = value["custom_model_deployment_arn"]
    out["modelDeploymentName"] = value["model_deployment_name"]
    out["modelArn"] = value["model_arn"]
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.custom_model_deployment_status

    out["status"] = aws_sdk_bedrock.types.custom_model_deployment_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "update_details" in value:
        import aws_sdk_bedrock.types.custom_model_deployment_update_details

        out["updateDetails"] = (
            aws_sdk_bedrock.types.custom_model_deployment_update_details.serialize_json(
                value["update_details"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "last_updated_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetCustomModelDeploymentResponse:
    out: GetCustomModelDeploymentResponse = {}  # type: ignore[typeddict-item]
    if "customModelDeploymentArn" in data:
        out["custom_model_deployment_arn"] = data["customModelDeploymentArn"]
    else:
        raise DeserializationError(
            "GetCustomModelDeploymentResponse.custom_model_deployment_arn required"
        )
    if "modelDeploymentName" in data:
        out["model_deployment_name"] = data["modelDeploymentName"]
    else:
        raise DeserializationError(
            "GetCustomModelDeploymentResponse.model_deployment_name required"
        )
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "GetCustomModelDeploymentResponse.model_arn required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "GetCustomModelDeploymentResponse.created_at required"
        )
    if "status" in data:
        import aws_sdk_bedrock.types.custom_model_deployment_status

        out["status"] = (
            aws_sdk_bedrock.types.custom_model_deployment_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetCustomModelDeploymentResponse.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "updateDetails" in data:
        import aws_sdk_bedrock.types.custom_model_deployment_update_details

        out["update_details"] = (
            aws_sdk_bedrock.types.custom_model_deployment_update_details.deserialize_json(
                data["updateDetails"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["last_updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
