"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LaunchTemplateConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.launch_template_configuration

LaunchTemplateConfigurationList: TypeAlias = list[
    "capo_imagebuilder.types.launch_template_configuration.LaunchTemplateConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateConfigurationList) -> list:
    import capo_imagebuilder.types.launch_template_configuration

    out: list = []
    for item in value:
        out.append(
            capo_imagebuilder.types.launch_template_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LaunchTemplateConfigurationList:
    import capo_imagebuilder.types.launch_template_configuration

    out: LaunchTemplateConfigurationList = []
    for item in data:
        out.append(
            capo_imagebuilder.types.launch_template_configuration.deserialize_json(item)
        )
    return out
