"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.control_mapping

ControlMappings: TypeAlias = list[
    "aws_sdk_controlcatalog.types.control_mapping.ControlMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlMappings) -> list:
    import aws_sdk_controlcatalog.types.control_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_controlcatalog.types.control_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlMappings:
    import aws_sdk_controlcatalog.types.control_mapping

    out: ControlMappings = []
    for item in data:
        out.append(aws_sdk_controlcatalog.types.control_mapping.deserialize_json(item))
    return out
