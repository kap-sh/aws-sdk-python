"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListStageDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.device_deployment_summaries
    import aws_sdk_sagemaker.types.next_token


class ListStageDevicesResponse(TypedDict, closed=True):
    device_deployment_summaries: NotRequired[
        "aws_sdk_sagemaker.types.device_deployment_summaries.DeviceDeploymentSummaries"
    ]
    """<p>List of summaries of devices allocated to the stage.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The token to use when calling the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStageDevicesResponse) -> dict:
    out: dict = {}
    if "device_deployment_summaries" in value:
        import aws_sdk_sagemaker.types.device_deployment_summaries

        out["DeviceDeploymentSummaries"] = (
            aws_sdk_sagemaker.types.device_deployment_summaries.serialize_aws_json_1_1(
                value["device_deployment_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStageDevicesResponse:
    out: ListStageDevicesResponse = {}  # type: ignore[typeddict-item]
    if "DeviceDeploymentSummaries" in data:
        import aws_sdk_sagemaker.types.device_deployment_summaries

        out["device_deployment_summaries"] = (
            aws_sdk_sagemaker.types.device_deployment_summaries.deserialize_aws_json_1_1(
                data["DeviceDeploymentSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
