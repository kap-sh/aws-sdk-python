"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_deployment_summary

CustomModelDeploymentSummaryList: TypeAlias = list[
    "aws_sdk_bedrock.types.custom_model_deployment_summary.CustomModelDeploymentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDeploymentSummaryList) -> list:
    import aws_sdk_bedrock.types.custom_model_deployment_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.custom_model_deployment_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CustomModelDeploymentSummaryList:
    import aws_sdk_bedrock.types.custom_model_deployment_summary

    out: CustomModelDeploymentSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.custom_model_deployment_summary.deserialize_json(item)
        )
    return out
