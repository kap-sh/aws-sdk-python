"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.container
    import capo_lightsail.types.container_name

ContainerMap: TypeAlias = dict[
    "capo_lightsail.types.container_name.ContainerName",
    "capo_lightsail.types.container.Container",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ContainerMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lightsail.types.container

        out[key] = capo_lightsail.types.container.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerMap:
    out: ContainerMap = {}
    for key, value in data.items():
        import capo_lightsail.types.container

        out[key] = capo_lightsail.types.container.deserialize_aws_json_1_1(value)
    return out
