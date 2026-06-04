"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_security_group

ManagedSecurityGroups: TypeAlias = list[
    "aws_sdk_ecs.types.managed_security_group.ManagedSecurityGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedSecurityGroups) -> list:
    import aws_sdk_ecs.types.managed_security_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.managed_security_group.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedSecurityGroups:
    import aws_sdk_ecs.types.managed_security_group

    out: ManagedSecurityGroups = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.managed_security_group.deserialize_aws_json_1_1(item)
        )
    return out
