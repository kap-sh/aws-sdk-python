"""Generated from Smithy shape ``com.amazonaws.connect#AllowedFlowModules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.flow_module

AllowedFlowModules: TypeAlias = list["aws_sdk_connect.types.flow_module.FlowModule"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedFlowModules) -> list:
    import aws_sdk_connect.types.flow_module

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.flow_module.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedFlowModules:
    import aws_sdk_connect.types.flow_module

    out: AllowedFlowModules = []
    for item in data:
        out.append(aws_sdk_connect.types.flow_module.deserialize_json(item))
    return out
