"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_action

FleetActionList: TypeAlias = list["aws_sdk_gamelift.types.fleet_action.FleetAction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetActionList) -> list:
    import aws_sdk_gamelift.types.fleet_action

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.fleet_action.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetActionList:
    import aws_sdk_gamelift.types.fleet_action

    out: FleetActionList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.fleet_action.deserialize_aws_json_1_1(item))
    return out
