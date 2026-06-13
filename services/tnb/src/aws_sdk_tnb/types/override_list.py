"""Generated from Smithy shape ``com.amazonaws.tnb#OverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_tnb.types.tosca_override

OverrideList: TypeAlias = list["aws_sdk_tnb.types.tosca_override.ToscaOverride"]


# --- restJson1 ser/de ---
def serialize_json(value: OverrideList) -> list:
    import aws_sdk_tnb.types.tosca_override

    out: list = []
    for item in value:
        out.append(aws_sdk_tnb.types.tosca_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> OverrideList:
    import aws_sdk_tnb.types.tosca_override

    out: OverrideList = []
    for item in data:
        out.append(aws_sdk_tnb.types.tosca_override.deserialize_json(item))
    return out
