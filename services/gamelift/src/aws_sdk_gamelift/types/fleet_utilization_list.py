"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetUtilizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_utilization

FleetUtilizationList: TypeAlias = list[
    "aws_sdk_gamelift.types.fleet_utilization.FleetUtilization"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetUtilizationList) -> list:
    import aws_sdk_gamelift.types.fleet_utilization

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.fleet_utilization.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FleetUtilizationList:
    import aws_sdk_gamelift.types.fleet_utilization

    out: FleetUtilizationList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.fleet_utilization.deserialize_aws_json_1_1(item)
        )
    return out
