"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_parameter

ComponentParameterList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.component_parameter.ComponentParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentParameterList) -> list:
    import aws_sdk_imagebuilder.types.component_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_imagebuilder.types.component_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentParameterList:
    import aws_sdk_imagebuilder.types.component_parameter

    out: ComponentParameterList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.component_parameter.deserialize_json(item)
        )
    return out
