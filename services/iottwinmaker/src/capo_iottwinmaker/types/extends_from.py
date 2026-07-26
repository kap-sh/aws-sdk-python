"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ExtendsFrom``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_type_id

ExtendsFrom: TypeAlias = list[
    "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtendsFrom) -> list:
    return list(value)


def deserialize_json(data: list) -> ExtendsFrom:
    return list(data)
