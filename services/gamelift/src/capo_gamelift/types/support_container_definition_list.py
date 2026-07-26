"""Generated from Smithy shape ``com.amazonaws.gamelift#SupportContainerDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.support_container_definition

SupportContainerDefinitionList: TypeAlias = list[
    "capo_gamelift.types.support_container_definition.SupportContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportContainerDefinitionList) -> list:
    import capo_gamelift.types.support_container_definition

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.support_container_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupportContainerDefinitionList:
    import capo_gamelift.types.support_container_definition

    out: SupportContainerDefinitionList = []
    for item in data:
        out.append(
            capo_gamelift.types.support_container_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
