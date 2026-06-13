"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentDeploymentDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_failure_reasons
    import aws_sdk_datazone.types.overall_deployment_status


class EnvironmentDeploymentDetails(TypedDict):
    overall_deployment_status: NotRequired[
        "aws_sdk_datazone.types.overall_deployment_status.OverallDeploymentStatus"
    ]
    """<p>The overall deployment status of the environment.</p>"""
    environment_failure_reasons: NotRequired[
        "aws_sdk_datazone.types.environment_failure_reasons.EnvironmentFailureReasons"
    ]
    """<p>Environment failure reasons.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentDeploymentDetails) -> dict:
    out: dict = {}
    if "overall_deployment_status" in value:
        import aws_sdk_datazone.types.overall_deployment_status

        out["overallDeploymentStatus"] = (
            aws_sdk_datazone.types.overall_deployment_status.serialize_json(
                value["overall_deployment_status"]
            )
        )
    if "environment_failure_reasons" in value:
        import aws_sdk_datazone.types.environment_failure_reasons

        out["environmentFailureReasons"] = (
            aws_sdk_datazone.types.environment_failure_reasons.serialize_json(
                value["environment_failure_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentDeploymentDetails:
    out: EnvironmentDeploymentDetails = {}  # type: ignore[typeddict-item]
    if "overallDeploymentStatus" in data:
        import aws_sdk_datazone.types.overall_deployment_status

        out["overall_deployment_status"] = (
            aws_sdk_datazone.types.overall_deployment_status.deserialize_json(
                data["overallDeploymentStatus"]
            )
        )
    if "environmentFailureReasons" in data:
        import aws_sdk_datazone.types.environment_failure_reasons

        out["environment_failure_reasons"] = (
            aws_sdk_datazone.types.environment_failure_reasons.deserialize_json(
                data["environmentFailureReasons"]
            )
        )
    return out
