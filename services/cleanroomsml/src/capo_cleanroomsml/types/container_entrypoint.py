"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ContainerEntrypoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.container_entrypoint_string

ContainerEntrypoint: TypeAlias = list[
    "capo_cleanroomsml.types.container_entrypoint_string.ContainerEntrypointString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerEntrypoint) -> list:
    return list(value)


def deserialize_json(data: list) -> ContainerEntrypoint:
    return list(data)
