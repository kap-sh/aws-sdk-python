"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerPortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_port_range

ContainerPortRangeList: TypeAlias = list[
    "aws_sdk_gamelift.types.container_port_range.ContainerPortRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerPortRangeList) -> list:
    import aws_sdk_gamelift.types.container_port_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.container_port_range.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerPortRangeList:
    import aws_sdk_gamelift.types.container_port_range

    out: ContainerPortRangeList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.container_port_range.deserialize_aws_json_1_1(item)
        )
    return out
