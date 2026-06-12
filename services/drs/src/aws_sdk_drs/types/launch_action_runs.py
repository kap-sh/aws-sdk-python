"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionRuns``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action_run

LaunchActionRuns: TypeAlias = list["aws_sdk_drs.types.launch_action_run.LaunchActionRun"]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchActionRuns) -> list:
    import aws_sdk_drs.types.launch_action_run
    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.launch_action_run.serialize_json(item))
    return out


def deserialize_json(data: list) -> LaunchActionRuns:
    import aws_sdk_drs.types.launch_action_run
    out: LaunchActionRuns = []
    for item in data:
        out.append(aws_sdk_drs.types.launch_action_run.deserialize_json(item))
    return out