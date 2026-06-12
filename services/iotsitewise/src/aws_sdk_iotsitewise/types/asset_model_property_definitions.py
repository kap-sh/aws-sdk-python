"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertyDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_property_definition

AssetModelPropertyDefinitions: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_model_property_definition.AssetModelPropertyDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertyDefinitions) -> list:
    import aws_sdk_iotsitewise.types.asset_model_property_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_property_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetModelPropertyDefinitions:
    import aws_sdk_iotsitewise.types.asset_model_property_definition

    out: AssetModelPropertyDefinitions = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_property_definition.deserialize_json(
                item
            )
        )
    return out
