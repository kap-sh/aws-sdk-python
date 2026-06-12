"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModelDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_composite_model_definition

AssetModelCompositeModelDefinitions: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_model_composite_model_definition.AssetModelCompositeModelDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModelDefinitions) -> list:
    import aws_sdk_iotsitewise.types.asset_model_composite_model_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_composite_model_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetModelCompositeModelDefinitions:
    import aws_sdk_iotsitewise.types.asset_model_composite_model_definition

    out: AssetModelCompositeModelDefinitions = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_composite_model_definition.deserialize_json(
                item
            )
        )
    return out
