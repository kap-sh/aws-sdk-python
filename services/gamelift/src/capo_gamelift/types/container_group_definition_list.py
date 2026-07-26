"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition

ContainerGroupDefinitionList: TypeAlias = list[
    "capo_gamelift.types.container_group_definition.ContainerGroupDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerGroupDefinitionList) -> list:
    import capo_gamelift.types.container_group_definition

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_group_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerGroupDefinitionList:
    import capo_gamelift.types.container_group_definition

    out: ContainerGroupDefinitionList = []
    for item in data:
        out.append(
            capo_gamelift.types.container_group_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
