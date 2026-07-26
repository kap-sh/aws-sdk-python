"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_put_asset_property_error

BatchPutAssetPropertyErrors: TypeAlias = list[
    "capo_iotsitewise.types.batch_put_asset_property_error.BatchPutAssetPropertyError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyErrors) -> list:
    import capo_iotsitewise.types.batch_put_asset_property_error

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.batch_put_asset_property_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchPutAssetPropertyErrors:
    import capo_iotsitewise.types.batch_put_asset_property_error

    out: BatchPutAssetPropertyErrors = []
    for item in data:
        out.append(
            capo_iotsitewise.types.batch_put_asset_property_error.deserialize_json(item)
        )
    return out
