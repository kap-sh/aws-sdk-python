"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedLogGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_log_group

ManagedLogGroups: TypeAlias = list[
    "aws_sdk_ecs.types.managed_log_group.ManagedLogGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedLogGroups) -> list:
    import aws_sdk_ecs.types.managed_log_group

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.managed_log_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedLogGroups:
    import aws_sdk_ecs.types.managed_log_group

    out: ManagedLogGroups = []
    for item in data:
        out.append(aws_sdk_ecs.types.managed_log_group.deserialize_aws_json_1_1(item))
    return out
