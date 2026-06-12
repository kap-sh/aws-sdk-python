"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_property

AssetModelProperties: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_model_property.AssetModelProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelProperties) -> list:
    import aws_sdk_iotsitewise.types.asset_model_property

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.asset_model_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetModelProperties:
    import aws_sdk_iotsitewise.types.asset_model_property

    out: AssetModelProperties = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_property.deserialize_json(item)
        )
    return out
