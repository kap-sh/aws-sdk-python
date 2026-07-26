"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_deployment
    import capo_gamelift.types.locational_deployments


class DescribeFleetDeploymentOutput(TypedDict, closed=True):
    fleet_deployment: NotRequired[
        "capo_gamelift.types.fleet_deployment.FleetDeployment"
    ]
    """<p>The requested deployment information.</p>"""
    locational_deployments: NotRequired[
        "capo_gamelift.types.locational_deployments.LocationalDeployments"
    ]
    """<p>If the deployment is for a multi-location fleet, the requests returns the deployment status in each fleet location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetDeploymentOutput) -> dict:
    out: dict = {}
    if "fleet_deployment" in value:
        import capo_gamelift.types.fleet_deployment

        out["FleetDeployment"] = (
            capo_gamelift.types.fleet_deployment.serialize_aws_json_1_1(
                value["fleet_deployment"]
            )
        )
    if "locational_deployments" in value:
        import capo_gamelift.types.locational_deployments

        out["LocationalDeployments"] = (
            capo_gamelift.types.locational_deployments.serialize_aws_json_1_1(
                value["locational_deployments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetDeploymentOutput:
    out: DescribeFleetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "FleetDeployment" in data:
        import capo_gamelift.types.fleet_deployment

        out["fleet_deployment"] = (
            capo_gamelift.types.fleet_deployment.deserialize_aws_json_1_1(
                data["FleetDeployment"]
            )
        )
    if "LocationalDeployments" in data:
        import capo_gamelift.types.locational_deployments

        out["locational_deployments"] = (
            capo_gamelift.types.locational_deployments.deserialize_aws_json_1_1(
                data["LocationalDeployments"]
            )
        )
    return out
