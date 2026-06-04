"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_override

ContainerOverrides: TypeAlias = list[
    "aws_sdk_ecs.types.container_override.ContainerOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerOverrides) -> list:
    import aws_sdk_ecs.types.container_override

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.container_override.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerOverrides:
    import aws_sdk_ecs.types.container_override

    out: ContainerOverrides = []
    for item in data:
        out.append(aws_sdk_ecs.types.container_override.deserialize_aws_json_1_1(item))
    return out
