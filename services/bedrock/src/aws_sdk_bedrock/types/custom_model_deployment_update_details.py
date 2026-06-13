"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentUpdateDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_deployment_update_status
    import aws_sdk_bedrock.types.model_arn


class CustomModelDeploymentUpdateDetails(TypedDict):
    model_arn: "aws_sdk_bedrock.types.model_arn.ModelArn"
    """<p> ARN of the new custom model being deployed as part of the update. </p>"""
    update_status: "aws_sdk_bedrock.types.custom_model_deployment_update_status.CustomModelDeploymentUpdateStatus"
    """<p> Current status of the deployment update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDeploymentUpdateDetails) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    import aws_sdk_bedrock.types.custom_model_deployment_update_status

    out["updateStatus"] = (
        aws_sdk_bedrock.types.custom_model_deployment_update_status.serialize_json(
            value["update_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomModelDeploymentUpdateDetails:
    out: CustomModelDeploymentUpdateDetails = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "CustomModelDeploymentUpdateDetails.model_arn required"
        )
    if "updateStatus" in data:
        import aws_sdk_bedrock.types.custom_model_deployment_update_status

        out["update_status"] = (
            aws_sdk_bedrock.types.custom_model_deployment_update_status.deserialize_json(
                data["updateStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CustomModelDeploymentUpdateDetails.update_status required"
        )
    return out
