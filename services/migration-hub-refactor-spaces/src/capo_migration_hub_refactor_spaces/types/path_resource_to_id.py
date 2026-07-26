"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#PathResourceToId``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.path_resource_to_id_key
    import capo_migration_hub_refactor_spaces.types.path_resource_to_id_value

PathResourceToId: TypeAlias = dict[
    "capo_migration_hub_refactor_spaces.types.path_resource_to_id_key.PathResourceToIdKey",
    "capo_migration_hub_refactor_spaces.types.path_resource_to_id_value.PathResourceToIdValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PathResourceToId) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PathResourceToId:
    out: PathResourceToId = {}
    for key, value in data.items():
        out[key] = value
    return out
