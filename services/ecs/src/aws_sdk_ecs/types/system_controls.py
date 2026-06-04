"""Generated from Smithy shape ``com.amazonaws.ecs#SystemControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.system_control

SystemControls: TypeAlias = list["aws_sdk_ecs.types.system_control.SystemControl"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemControls) -> list:
    import aws_sdk_ecs.types.system_control

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.system_control.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SystemControls:
    import aws_sdk_ecs.types.system_control

    out: SystemControls = []
    for item in data:
        out.append(aws_sdk_ecs.types.system_control.deserialize_aws_json_1_1(item))
    return out
