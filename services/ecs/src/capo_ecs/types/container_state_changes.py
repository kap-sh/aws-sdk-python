"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerStateChanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.container_state_change

ContainerStateChanges: TypeAlias = list[
    "capo_ecs.types.container_state_change.ContainerStateChange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerStateChanges) -> list:
    import capo_ecs.types.container_state_change

    out: list = []
    for item in value:
        out.append(capo_ecs.types.container_state_change.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerStateChanges:
    import capo_ecs.types.container_state_change

    out: ContainerStateChanges = []
    for item in data:
        out.append(capo_ecs.types.container_state_change.deserialize_aws_json_1_1(item))
    return out
