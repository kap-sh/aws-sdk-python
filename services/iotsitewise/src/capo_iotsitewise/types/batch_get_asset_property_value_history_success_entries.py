"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistorySuccessEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_success_entry

BatchGetAssetPropertyValueHistorySuccessEntries: TypeAlias = list[
    "capo_iotsitewise.types.batch_get_asset_property_value_history_success_entry.BatchGetAssetPropertyValueHistorySuccessEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistorySuccessEntries) -> list:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_success_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_history_success_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueHistorySuccessEntries:
    import capo_iotsitewise.types.batch_get_asset_property_value_history_success_entry

    out: BatchGetAssetPropertyValueHistorySuccessEntries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_history_success_entry.deserialize_json(
                item
            )
        )
    return out
