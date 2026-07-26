"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_value_entry

BatchGetAssetPropertyValueEntries: TypeAlias = list[
    "capo_iotsitewise.types.batch_get_asset_property_value_entry.BatchGetAssetPropertyValueEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueEntries) -> list:
    import capo_iotsitewise.types.batch_get_asset_property_value_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueEntries:
    import capo_iotsitewise.types.batch_get_asset_property_value_entry

    out: BatchGetAssetPropertyValueEntries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_entry.deserialize_json(
                item
            )
        )
    return out
