"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetDeployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_deployment

FleetDeployments: TypeAlias = list[
    "aws_sdk_gamelift.types.fleet_deployment.FleetDeployment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetDeployments) -> list:
    import aws_sdk_gamelift.types.fleet_deployment

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.fleet_deployment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetDeployments:
    import aws_sdk_gamelift.types.fleet_deployment

    out: FleetDeployments = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.fleet_deployment.deserialize_aws_json_1_1(item)
        )
    return out
