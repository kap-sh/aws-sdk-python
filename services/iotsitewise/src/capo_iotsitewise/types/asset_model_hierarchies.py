"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelHierarchies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_hierarchy

AssetModelHierarchies: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_hierarchy.AssetModelHierarchy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelHierarchies) -> list:
    import capo_iotsitewise.types.asset_model_hierarchy

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.asset_model_hierarchy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetModelHierarchies:
    import capo_iotsitewise.types.asset_model_hierarchy

    out: AssetModelHierarchies = []
    for item in data:
        out.append(capo_iotsitewise.types.asset_model_hierarchy.deserialize_json(item))
    return out
