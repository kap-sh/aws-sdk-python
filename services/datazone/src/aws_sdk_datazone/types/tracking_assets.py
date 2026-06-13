"""Generated from Smithy shape ``com.amazonaws.datazone#TrackingAssets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.sage_maker_asset_type
    import aws_sdk_datazone.types.tracking_asset_arns

TrackingAssets: TypeAlias = dict[
    "aws_sdk_datazone.types.sage_maker_asset_type.SageMakerAssetType",
    "aws_sdk_datazone.types.tracking_asset_arns.TrackingAssetArns",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TrackingAssets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_datazone.types.tracking_asset_arns

        out[key] = aws_sdk_datazone.types.tracking_asset_arns.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TrackingAssets:
    out: TrackingAssets = {}
    for key, value in data.items():
        import aws_sdk_datazone.types.tracking_asset_arns

        out[key] = aws_sdk_datazone.types.tracking_asset_arns.deserialize_json(value)
    return out
