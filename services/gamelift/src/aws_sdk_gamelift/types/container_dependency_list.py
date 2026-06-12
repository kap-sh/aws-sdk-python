"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerDependencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_dependency

ContainerDependencyList: TypeAlias = list[
    "aws_sdk_gamelift.types.container_dependency.ContainerDependency"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDependencyList) -> list:
    import aws_sdk_gamelift.types.container_dependency

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.container_dependency.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerDependencyList:
    import aws_sdk_gamelift.types.container_dependency

    out: ContainerDependencyList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.container_dependency.deserialize_aws_json_1_1(item)
        )
    return out
