"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_fleet

ContainerFleetList: TypeAlias = list[
    "aws_sdk_gamelift.types.container_fleet.ContainerFleet"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleetList) -> list:
    import aws_sdk_gamelift.types.container_fleet

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.container_fleet.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerFleetList:
    import aws_sdk_gamelift.types.container_fleet

    out: ContainerFleetList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.container_fleet.deserialize_aws_json_1_1(item)
        )
    return out
