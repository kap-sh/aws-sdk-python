"""Generated from Smithy shape ``com.amazonaws.apprunner#StartDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn


class StartDeploymentRequest(TypedDict):
    service_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service that you want to manually deploy to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDeploymentRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDeploymentRequest:
    out: StartDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    else:
        raise DeserializationError("StartDeploymentRequest.service_arn required")
    return out
