"""Generated from Smithy shape ``com.amazonaws.gamelift#ListFleetDeploymentsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_deployments
    import aws_sdk_gamelift.types.non_zero_and_max_string


class ListFleetDeploymentsOutput(TypedDict):
    fleet_deployments: NotRequired[
        "aws_sdk_gamelift.types.fleet_deployments.FleetDeployments"
    ]
    """<p>The requested deployment information.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFleetDeploymentsOutput) -> dict:
    out: dict = {}
    if "fleet_deployments" in value:
        import aws_sdk_gamelift.types.fleet_deployments

        out["FleetDeployments"] = (
            aws_sdk_gamelift.types.fleet_deployments.serialize_aws_json_1_1(
                value["fleet_deployments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFleetDeploymentsOutput:
    out: ListFleetDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if "FleetDeployments" in data:
        import aws_sdk_gamelift.types.fleet_deployments

        out["fleet_deployments"] = (
            aws_sdk_gamelift.types.fleet_deployments.deserialize_aws_json_1_1(
                data["FleetDeployments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
