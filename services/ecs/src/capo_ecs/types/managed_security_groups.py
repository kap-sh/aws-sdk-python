"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.managed_security_group

ManagedSecurityGroups: TypeAlias = list[
    "capo_ecs.types.managed_security_group.ManagedSecurityGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedSecurityGroups) -> list:
    import capo_ecs.types.managed_security_group

    out: list = []
    for item in value:
        out.append(capo_ecs.types.managed_security_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedSecurityGroups:
    import capo_ecs.types.managed_security_group

    out: ManagedSecurityGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.managed_security_group.deserialize_aws_json_1_1(item))
    return out
