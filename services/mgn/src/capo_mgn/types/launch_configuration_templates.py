"""Generated from Smithy shape ``com.amazonaws.mgn#LaunchConfigurationTemplates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.launch_configuration_template

LaunchConfigurationTemplates: TypeAlias = list[
    "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchConfigurationTemplates) -> list:
    import capo_mgn.types.launch_configuration_template

    out: list = []
    for item in value:
        out.append(capo_mgn.types.launch_configuration_template.serialize_json(item))
    return out


def deserialize_json(data: list) -> LaunchConfigurationTemplates:
    import capo_mgn.types.launch_configuration_template

    out: LaunchConfigurationTemplates = []
    for item in data:
        out.append(capo_mgn.types.launch_configuration_template.deserialize_json(item))
    return out
