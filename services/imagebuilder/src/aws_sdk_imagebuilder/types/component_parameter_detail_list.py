"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentParameterDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_parameter_detail

ComponentParameterDetailList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.component_parameter_detail.ComponentParameterDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentParameterDetailList) -> list:
    import aws_sdk_imagebuilder.types.component_parameter_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.component_parameter_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComponentParameterDetailList:
    import aws_sdk_imagebuilder.types.component_parameter_detail

    out: ComponentParameterDetailList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.component_parameter_detail.deserialize_json(item)
        )
    return out
