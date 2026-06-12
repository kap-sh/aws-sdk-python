"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceDeploymentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.device_deployment_summary

DeviceDeploymentSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.device_deployment_summary.DeviceDeploymentSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceDeploymentSummaries) -> list:
    import aws_sdk_sagemaker.types.device_deployment_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.device_deployment_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceDeploymentSummaries:
    import aws_sdk_sagemaker.types.device_deployment_summary

    out: DeviceDeploymentSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.device_deployment_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
