"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ContainerArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.container_argument

ContainerArguments: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.container_argument.ContainerArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerArguments) -> list:
    return list(value)


def deserialize_json(data: list) -> ContainerArguments:
    return list(data)
