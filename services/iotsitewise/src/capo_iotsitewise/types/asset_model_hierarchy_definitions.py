"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelHierarchyDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_hierarchy_definition

AssetModelHierarchyDefinitions: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_hierarchy_definition.AssetModelHierarchyDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelHierarchyDefinitions) -> list:
    import capo_iotsitewise.types.asset_model_hierarchy_definition

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.asset_model_hierarchy_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetModelHierarchyDefinitions:
    import capo_iotsitewise.types.asset_model_hierarchy_definition

    out: AssetModelHierarchyDefinitions = []
    for item in data:
        out.append(
            capo_iotsitewise.types.asset_model_hierarchy_definition.deserialize_json(
                item
            )
        )
    return out
