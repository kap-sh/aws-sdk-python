"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationalDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.deployment_status


class LocationalDeployment(TypedDict, closed=True):
    deployment_status: NotRequired[
        "capo_gamelift.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of fleet deployment activity in the location. </p> <ul> <li> <p> <code>IN_PROGRESS</code> -- The deployment is in progress.</p> </li> <li> <p> <code>IMPAIRED</code> -- The deployment failed and the fleet has some impaired containers. </p> </li> <li> <p> <code>COMPLETE</code> -- The deployment has completed successfully.</p> </li> <li> <p> <code>ROLLBACK_IN_PROGRESS</code> -- The deployment failed and rollback has been initiated.</p> </li> <li> <p> <code>ROLLBACK_IN_COMPLETE</code> -- The deployment failed and rollback has been completed.</p> </li> <li> <p> <code>CANCELLED</code> -- The deployment was cancelled.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationalDeployment) -> dict:
    out: dict = {}
    if "deployment_status" in value:
        import capo_gamelift.types.deployment_status

        out["DeploymentStatus"] = (
            capo_gamelift.types.deployment_status.serialize_aws_json_1_1(
                value["deployment_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationalDeployment:
    out: LocationalDeployment = {}  # type: ignore[typeddict-item]
    if "DeploymentStatus" in data:
        import capo_gamelift.types.deployment_status

        out["deployment_status"] = (
            capo_gamelift.types.deployment_status.deserialize_aws_json_1_1(
                data["DeploymentStatus"]
            )
        )
    return out
