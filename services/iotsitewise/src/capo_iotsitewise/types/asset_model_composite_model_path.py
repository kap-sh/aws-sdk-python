"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModelPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_model_path_segment

AssetModelCompositeModelPath: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_composite_model_path_segment.AssetModelCompositeModelPathSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModelPath) -> list:
    import capo_iotsitewise.types.asset_model_composite_model_path_segment

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.asset_model_composite_model_path_segment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetModelCompositeModelPath:
    import capo_iotsitewise.types.asset_model_composite_model_path_segment

    out: AssetModelCompositeModelPath = []
    for item in data:
        out.append(
            capo_iotsitewise.types.asset_model_composite_model_path_segment.deserialize_json(
                item
            )
        )
    return out
