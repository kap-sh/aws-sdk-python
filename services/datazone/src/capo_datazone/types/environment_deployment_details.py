"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentDeploymentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.environment_failure_reasons
    import capo_datazone.types.overall_deployment_status


class EnvironmentDeploymentDetails(TypedDict, closed=True):
    overall_deployment_status: NotRequired[
        "capo_datazone.types.overall_deployment_status.OverallDeploymentStatus"
    ]
    """<p>The overall deployment status of the environment.</p>"""
    environment_failure_reasons: NotRequired[
        "capo_datazone.types.environment_failure_reasons.EnvironmentFailureReasons"
    ]
    """<p>Environment failure reasons.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentDeploymentDetails) -> dict:
    out: dict = {}
    if "overall_deployment_status" in value:
        import capo_datazone.types.overall_deployment_status

        out["overallDeploymentStatus"] = (
            capo_datazone.types.overall_deployment_status.serialize_json(
                value["overall_deployment_status"]
            )
        )
    if "environment_failure_reasons" in value:
        import capo_datazone.types.environment_failure_reasons

        out["environmentFailureReasons"] = (
            capo_datazone.types.environment_failure_reasons.serialize_json(
                value["environment_failure_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentDeploymentDetails:
    out: EnvironmentDeploymentDetails = {}  # type: ignore[typeddict-item]
    if "overallDeploymentStatus" in data:
        import capo_datazone.types.overall_deployment_status

        out["overall_deployment_status"] = (
            capo_datazone.types.overall_deployment_status.deserialize_json(
                data["overallDeploymentStatus"]
            )
        )
    if "environmentFailureReasons" in data:
        import capo_datazone.types.environment_failure_reasons

        out["environment_failure_reasons"] = (
            capo_datazone.types.environment_failure_reasons.deserialize_json(
                data["environmentFailureReasons"]
            )
        )
    return out
