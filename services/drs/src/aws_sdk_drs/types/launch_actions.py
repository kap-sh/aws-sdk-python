"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action

LaunchActions: TypeAlias = list["aws_sdk_drs.types.launch_action.LaunchAction"]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchActions) -> list:
    import aws_sdk_drs.types.launch_action

    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.launch_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> LaunchActions:
    import aws_sdk_drs.types.launch_action

    out: LaunchActions = []
    for item in data:
        out.append(aws_sdk_drs.types.launch_action.deserialize_json(item))
    return out
