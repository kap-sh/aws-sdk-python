"""Generated from Smithy shape ``com.amazonaws.ecs#StopServiceDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class StopServiceDeploymentResponse(TypedDict, closed=True):
    service_deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the stopped service deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopServiceDeploymentResponse) -> dict:
    out: dict = {}
    if "service_deployment_arn" in value:
        out["serviceDeploymentArn"] = value["service_deployment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopServiceDeploymentResponse:
    out: StopServiceDeploymentResponse = {}  # type: ignore[typeddict-item]
    if "serviceDeploymentArn" in data:
        out["service_deployment_arn"] = data["serviceDeploymentArn"]
    return out
