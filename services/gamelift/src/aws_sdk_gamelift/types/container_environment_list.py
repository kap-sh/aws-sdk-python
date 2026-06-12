"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerEnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_environment

ContainerEnvironmentList: TypeAlias = list[
    "aws_sdk_gamelift.types.container_environment.ContainerEnvironment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerEnvironmentList) -> list:
    import aws_sdk_gamelift.types.container_environment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.container_environment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerEnvironmentList:
    import aws_sdk_gamelift.types.container_environment

    out: ContainerEnvironmentList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.container_environment.deserialize_aws_json_1_1(item)
        )
    return out
