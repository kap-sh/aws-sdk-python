"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupConfigurationParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_configuration_parameter_value

GroupConfigurationParameterValueList: TypeAlias = list[
    "aws_sdk_resource_groups.types.group_configuration_parameter_value.GroupConfigurationParameterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupConfigurationParameterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupConfigurationParameterValueList:
    return list(data)
