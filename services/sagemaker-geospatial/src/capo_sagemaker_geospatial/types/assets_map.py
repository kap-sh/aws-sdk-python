"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#AssetsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.asset_value

AssetsMap: TypeAlias = dict[
    "str", "capo_sagemaker_geospatial.types.asset_value.AssetValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AssetsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker_geospatial.types.asset_value

        out[key] = capo_sagemaker_geospatial.types.asset_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AssetsMap:
    out: AssetsMap = {}
    for key, value in data.items():
        import capo_sagemaker_geospatial.types.asset_value

        out[key] = capo_sagemaker_geospatial.types.asset_value.deserialize_json(value)
    return out
