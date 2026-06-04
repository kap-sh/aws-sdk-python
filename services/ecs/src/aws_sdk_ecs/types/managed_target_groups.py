"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedTargetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_target_group

ManagedTargetGroups: TypeAlias = list[
    "aws_sdk_ecs.types.managed_target_group.ManagedTargetGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedTargetGroups) -> list:
    import aws_sdk_ecs.types.managed_target_group

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.managed_target_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedTargetGroups:
    import aws_sdk_ecs.types.managed_target_group

    out: ManagedTargetGroups = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.managed_target_group.deserialize_aws_json_1_1(item)
        )
    return out
