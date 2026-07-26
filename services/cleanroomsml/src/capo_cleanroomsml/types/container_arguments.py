"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ContainerArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.container_argument

ContainerArguments: TypeAlias = list[
    "capo_cleanroomsml.types.container_argument.ContainerArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerArguments) -> list:
    return list(value)


def deserialize_json(data: list) -> ContainerArguments:
    return list(data)
