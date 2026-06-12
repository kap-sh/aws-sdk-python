"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_composite_model

AssetModelCompositeModels: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_model_composite_model.AssetModelCompositeModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModels) -> list:
    import aws_sdk_iotsitewise.types.asset_model_composite_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_composite_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetModelCompositeModels:
    import aws_sdk_iotsitewise.types.asset_model_composite_model

    out: AssetModelCompositeModels = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_model_composite_model.deserialize_json(item)
        )
    return out
