"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_capacity

FleetCapacityList: TypeAlias = list["capo_gamelift.types.fleet_capacity.FleetCapacity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetCapacityList) -> list:
    import capo_gamelift.types.fleet_capacity

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.fleet_capacity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetCapacityList:
    import capo_gamelift.types.fleet_capacity

    out: FleetCapacityList = []
    for item in data:
        out.append(capo_gamelift.types.fleet_capacity.deserialize_aws_json_1_1(item))
    return out
