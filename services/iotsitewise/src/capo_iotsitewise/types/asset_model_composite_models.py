"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_model

AssetModelCompositeModels: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_composite_model.AssetModelCompositeModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModels) -> list:
    import capo_iotsitewise.types.asset_model_composite_model

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.asset_model_composite_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetModelCompositeModels:
    import capo_iotsitewise.types.asset_model_composite_model

    out: AssetModelCompositeModels = []
    for item in data:
        out.append(
            capo_iotsitewise.types.asset_model_composite_model.deserialize_json(item)
        )
    return out
