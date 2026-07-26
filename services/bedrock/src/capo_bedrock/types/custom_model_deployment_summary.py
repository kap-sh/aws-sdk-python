"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_deployment_arn
    import capo_bedrock.types.custom_model_deployment_status
    import capo_bedrock.types.error_message
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.model_deployment_name
    import capo_bedrock.types.timestamp


class CustomModelDeploymentSummary(TypedDict, closed=True):
    custom_model_deployment_arn: (
        "capo_bedrock.types.custom_model_deployment_arn.CustomModelDeploymentArn"
    )
    """<p>The Amazon Resource Name (ARN) of the custom model deployment.</p>"""
    custom_model_deployment_name: (
        "capo_bedrock.types.model_deployment_name.ModelDeploymentName"
    )
    """<p>The name of the custom model deployment.</p>"""
    model_arn: "capo_bedrock.types.model_arn.ModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model associated with this deployment.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The date and time when the custom model deployment was created.</p>"""
    status: (
        "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
    )
    """<p>The status of the custom model deployment. Possible values are <code>CREATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>"""
    last_updated_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The date and time when the custom model deployment was last modified.</p>"""
    failure_message: NotRequired["capo_bedrock.types.error_message.ErrorMessage"]
    """<p>If the deployment status is <code>FAILED</code>, this field contains a message describing the failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDeploymentSummary) -> dict:
    out: dict = {}
    out["customModelDeploymentArn"] = value["custom_model_deployment_arn"]
    out["customModelDeploymentName"] = value["custom_model_deployment_name"]
    out["modelArn"] = value["model_arn"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.custom_model_deployment_status

    out["status"] = capo_bedrock.types.custom_model_deployment_status.serialize_json(
        value["status"]
    )
    if "last_updated_at" in value:
        import capo_bedrock.types.timestamp

        out["lastUpdatedAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> CustomModelDeploymentSummary:
    out: CustomModelDeploymentSummary = {}  # type: ignore[typeddict-item]
    if "customModelDeploymentArn" in data:
        out["custom_model_deployment_arn"] = data["customModelDeploymentArn"]
    else:
        raise DeserializationError(
            "CustomModelDeploymentSummary.custom_model_deployment_arn required"
        )
    if "customModelDeploymentName" in data:
        out["custom_model_deployment_name"] = data["customModelDeploymentName"]
    else:
        raise DeserializationError(
            "CustomModelDeploymentSummary.custom_model_deployment_name required"
        )
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("CustomModelDeploymentSummary.model_arn required")
    if "createdAt" in data:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CustomModelDeploymentSummary.created_at required")
    if "status" in data:
        import capo_bedrock.types.custom_model_deployment_status

        out["status"] = (
            capo_bedrock.types.custom_model_deployment_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CustomModelDeploymentSummary.status required")
    if "lastUpdatedAt" in data:
        import capo_bedrock.types.timestamp

        out["last_updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
