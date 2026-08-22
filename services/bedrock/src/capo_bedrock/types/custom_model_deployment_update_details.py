"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentUpdateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_deployment_update_status
    import capo_bedrock.types.model_arn


class CustomModelDeploymentUpdateDetails(TypedDict, closed=True):
    model_arn: "capo_bedrock.types.model_arn.ModelArn"
    """<p> ARN of the new custom model being deployed as part of the update. </p>"""
    update_status: "capo_bedrock.types.custom_model_deployment_update_status.CustomModelDeploymentUpdateStatus"
    """<p> Current status of the deployment update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDeploymentUpdateDetails) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    import capo_bedrock.types.custom_model_deployment_update_status

    out["updateStatus"] = (
        capo_bedrock.types.custom_model_deployment_update_status.serialize_json(
            value["update_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomModelDeploymentUpdateDetails:
    out: CustomModelDeploymentUpdateDetails = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "CustomModelDeploymentUpdateDetails.model_arn required"
        )
    if data.get("updateStatus") is not None:
        import capo_bedrock.types.custom_model_deployment_update_status

        out["update_status"] = (
            capo_bedrock.types.custom_model_deployment_update_status.deserialize_json(
                data["updateStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CustomModelDeploymentUpdateDetails.update_status required"
        )
    return out
