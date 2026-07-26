"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelsTypeFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_type

ListAssetModelsTypeFilter: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_type.AssetModelType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetModelsTypeFilter) -> list:
    import capo_iotsitewise.types.asset_model_type

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.asset_model_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListAssetModelsTypeFilter:
    import capo_iotsitewise.types.asset_model_type

    out: ListAssetModelsTypeFilter = []
    for item in data:
        out.append(capo_iotsitewise.types.asset_model_type.deserialize_json(item))
    return out
