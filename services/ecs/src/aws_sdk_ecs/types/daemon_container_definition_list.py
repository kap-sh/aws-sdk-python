"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_container_definition

DaemonContainerDefinitionList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_container_definition.DaemonContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonContainerDefinitionList) -> list:
    import aws_sdk_ecs.types.daemon_container_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.daemon_container_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonContainerDefinitionList:
    import aws_sdk_ecs.types.daemon_container_definition

    out: DaemonContainerDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.daemon_container_definition.deserialize_aws_json_1_1(item)
        )
    return out
