"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_configuration

ComponentConfigurationList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.component_configuration.ComponentConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConfigurationList) -> list:
    import aws_sdk_imagebuilder.types.component_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.component_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComponentConfigurationList:
    import aws_sdk_imagebuilder.types.component_configuration

    out: ComponentConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.component_configuration.deserialize_json(item)
        )
    return out
