"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.control_parameter

ControlParameters: TypeAlias = list[
    "aws_sdk_controlcatalog.types.control_parameter.ControlParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlParameters) -> list:
    import aws_sdk_controlcatalog.types.control_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_controlcatalog.types.control_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlParameters:
    import aws_sdk_controlcatalog.types.control_parameter

    out: ControlParameters = []
    for item in data:
        out.append(
            aws_sdk_controlcatalog.types.control_parameter.deserialize_json(item)
        )
    return out
