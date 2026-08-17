"""Generated from Smithy shape ``com.amazonaws.ecs#SystemControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.system_control

SystemControls: TypeAlias = list["capo_ecs.types.system_control.SystemControl"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemControls) -> list:
    import capo_ecs.types.system_control

    out: list = []
    for item in value:
        out.append(capo_ecs.types.system_control.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SystemControls:
    import capo_ecs.types.system_control

    out: SystemControls = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.system_control.deserialize_aws_json_1_1(item))
    return out
