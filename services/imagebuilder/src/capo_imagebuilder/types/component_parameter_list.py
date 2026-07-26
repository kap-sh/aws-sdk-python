"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_parameter

ComponentParameterList: TypeAlias = list[
    "capo_imagebuilder.types.component_parameter.ComponentParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentParameterList) -> list:
    import capo_imagebuilder.types.component_parameter

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.component_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentParameterList:
    import capo_imagebuilder.types.component_parameter

    out: ComponentParameterList = []
    for item in data:
        out.append(capo_imagebuilder.types.component_parameter.deserialize_json(item))
    return out
