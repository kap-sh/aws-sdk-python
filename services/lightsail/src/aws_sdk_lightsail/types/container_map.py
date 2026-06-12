"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container
    import aws_sdk_lightsail.types.container_name

ContainerMap: TypeAlias = dict[
    "aws_sdk_lightsail.types.container_name.ContainerName",
    "aws_sdk_lightsail.types.container.Container",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ContainerMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_lightsail.types.container

        out[key] = aws_sdk_lightsail.types.container.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerMap:
    out: ContainerMap = {}
    for key, value in data.items():
        import aws_sdk_lightsail.types.container

        out[key] = aws_sdk_lightsail.types.container.deserialize_aws_json_1_1(value)
    return out
