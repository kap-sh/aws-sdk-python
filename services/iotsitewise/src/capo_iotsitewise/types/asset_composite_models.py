"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetCompositeModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_composite_model

AssetCompositeModels: TypeAlias = list[
    "capo_iotsitewise.types.asset_composite_model.AssetCompositeModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetCompositeModels) -> list:
    import capo_iotsitewise.types.asset_composite_model

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.asset_composite_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetCompositeModels:
    import capo_iotsitewise.types.asset_composite_model

    out: AssetCompositeModels = []
    for item in data:
        out.append(capo_iotsitewise.types.asset_composite_model.deserialize_json(item))
    return out
