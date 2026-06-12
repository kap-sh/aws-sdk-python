"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelHierarchyDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_hierarchy_definition

AssetModelHierarchyDefinitions: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_model_hierarchy_definition.AssetModelHierarchyDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelHierarchyDefinitions) -> list:
    import aws_sdk_iotsitewise.types.asset_model_hierarchy_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_hierarchy_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetModelHierarchyDefinitions:
    import aws_sdk_iotsitewise.types.asset_model_hierarchy_definition

    out: AssetModelHierarchyDefinitions = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_hierarchy_definition.deserialize_json(
                item
            )
        )
    return out
