"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedTargetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.managed_target_group

ManagedTargetGroups: TypeAlias = list[
    "capo_ecs.types.managed_target_group.ManagedTargetGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedTargetGroups) -> list:
    import capo_ecs.types.managed_target_group

    out: list = []
    for item in value:
        out.append(capo_ecs.types.managed_target_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedTargetGroups:
    import capo_ecs.types.managed_target_group

    out: ManagedTargetGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.managed_target_group.deserialize_aws_json_1_1(item))
    return out
