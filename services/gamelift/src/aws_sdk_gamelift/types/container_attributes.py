"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_attribute

ContainerAttributes: TypeAlias = list[
    "aws_sdk_gamelift.types.container_attribute.ContainerAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerAttributes) -> list:
    import aws_sdk_gamelift.types.container_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.container_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerAttributes:
    import aws_sdk_gamelift.types.container_attribute

    out: ContainerAttributes = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.container_attribute.deserialize_aws_json_1_1(item)
        )
    return out
