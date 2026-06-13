"""Generated from Smithy shape ``com.amazonaws.drs#LaunchConfigurationTemplateIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_configuration_template_id

LaunchConfigurationTemplateIDs: TypeAlias = list[
    "aws_sdk_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchConfigurationTemplateIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> LaunchConfigurationTemplateIDs:
    return list(data)
