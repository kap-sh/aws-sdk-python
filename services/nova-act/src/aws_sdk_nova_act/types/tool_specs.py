"""Generated from Smithy shape ``com.amazonaws.novaact#ToolSpecs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.tool_spec

ToolSpecs: TypeAlias = list["aws_sdk_nova_act.types.tool_spec.ToolSpec"]


# --- restJson1 ser/de ---
def serialize_json(value: ToolSpecs) -> list:
    import aws_sdk_nova_act.types.tool_spec

    out: list = []
    for item in value:
        out.append(aws_sdk_nova_act.types.tool_spec.serialize_json(item))
    return out


def deserialize_json(data: list) -> ToolSpecs:
    import aws_sdk_nova_act.types.tool_spec

    out: ToolSpecs = []
    for item in data:
        out.append(aws_sdk_nova_act.types.tool_spec.deserialize_json(item))
    return out
