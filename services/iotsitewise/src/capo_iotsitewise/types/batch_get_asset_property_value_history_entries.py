"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistoryEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_entry

BatchGetAssetPropertyValueHistoryEntries: TypeAlias = list[
    "capo_iotsitewise.types.batch_get_asset_property_value_history_entry.BatchGetAssetPropertyValueHistoryEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistoryEntries) -> list:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_history_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueHistoryEntries:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_entry

    out: BatchGetAssetPropertyValueHistoryEntries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_history_entry.deserialize_json(
                item
            )
        )
    return out
