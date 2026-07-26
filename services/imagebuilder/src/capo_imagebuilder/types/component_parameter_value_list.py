"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_parameter_value

ComponentParameterValueList: TypeAlias = list[
    "capo_imagebuilder.types.component_parameter_value.ComponentParameterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentParameterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ComponentParameterValueList:
    return list(data)
