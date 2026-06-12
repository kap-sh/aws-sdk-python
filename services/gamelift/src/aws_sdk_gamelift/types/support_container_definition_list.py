"""Generated from Smithy shape ``com.amazonaws.gamelift#SupportContainerDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.support_container_definition

SupportContainerDefinitionList: TypeAlias = list[
    "aws_sdk_gamelift.types.support_container_definition.SupportContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportContainerDefinitionList) -> list:
    import aws_sdk_gamelift.types.support_container_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.support_container_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupportContainerDefinitionList:
    import aws_sdk_gamelift.types.support_container_definition

    out: SupportContainerDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.support_container_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
