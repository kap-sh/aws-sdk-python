"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertyPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_property_path_segment

AssetModelPropertyPath: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_property_path_segment.AssetModelPropertyPathSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertyPath) -> list:
    import capo_iotsitewise.types.asset_model_property_path_segment

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.asset_model_property_path_segment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetModelPropertyPath:
    import capo_iotsitewise.types.asset_model_property_path_segment

    out: AssetModelPropertyPath = []
    for item in data:
        out.append(
            capo_iotsitewise.types.asset_model_property_path_segment.deserialize_json(
                item
            )
        )
    return out
