"""Generated from Smithy shape ``com.amazonaws.gamelift#SupportContainerDefinitionInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.support_container_definition_input

SupportContainerDefinitionInputList: TypeAlias = list[
    "aws_sdk_gamelift.types.support_container_definition_input.SupportContainerDefinitionInput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportContainerDefinitionInputList) -> list:
    import aws_sdk_gamelift.types.support_container_definition_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.support_container_definition_input.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupportContainerDefinitionInputList:
    import aws_sdk_gamelift.types.support_container_definition_input

    out: SupportContainerDefinitionInputList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.support_container_definition_input.deserialize_aws_json_1_1(
                item
            )
        )
    return out
