"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistoryErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_error_entry

BatchGetAssetPropertyValueHistoryErrorEntries: TypeAlias = list[
    "capo_iotsitewise.types.batch_get_asset_property_value_history_error_entry.BatchGetAssetPropertyValueHistoryErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistoryErrorEntries) -> list:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_history_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueHistoryErrorEntries:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_error_entry

    out: BatchGetAssetPropertyValueHistoryErrorEntries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_history_error_entry.deserialize_json(
                item
            )
        )
    return out
