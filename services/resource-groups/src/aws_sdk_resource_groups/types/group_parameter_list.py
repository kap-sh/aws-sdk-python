"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_configuration_parameter

GroupParameterList: TypeAlias = list[
    "aws_sdk_resource_groups.types.group_configuration_parameter.GroupConfigurationParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupParameterList) -> list:
    import aws_sdk_resource_groups.types.group_configuration_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_groups.types.group_configuration_parameter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GroupParameterList:
    import aws_sdk_resource_groups.types.group_configuration_parameter

    out: GroupParameterList = []
    for item in data:
        out.append(
            aws_sdk_resource_groups.types.group_configuration_parameter.deserialize_json(
                item
            )
        )
    return out
