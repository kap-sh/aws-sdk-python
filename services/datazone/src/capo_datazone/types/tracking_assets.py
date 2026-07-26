"""Generated from Smithy shape ``com.amazonaws.datazone#TrackingAssets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.sage_maker_asset_type
    import capo_datazone.types.tracking_asset_arns

TrackingAssets: TypeAlias = dict[
    "capo_datazone.types.sage_maker_asset_type.SageMakerAssetType",
    "capo_datazone.types.tracking_asset_arns.TrackingAssetArns",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TrackingAssets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_datazone.types.tracking_asset_arns

        out[key] = capo_datazone.types.tracking_asset_arns.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TrackingAssets:
    out: TrackingAssets = {}
    for key, value in data.items():
        import capo_datazone.types.tracking_asset_arns

        out[key] = capo_datazone.types.tracking_asset_arns.deserialize_json(value)
    return out
