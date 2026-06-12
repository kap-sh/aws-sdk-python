"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistorySkippedEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_skipped_entry

BatchGetAssetPropertyValueHistorySkippedEntries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_skipped_entry.BatchGetAssetPropertyValueHistorySkippedEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistorySkippedEntries) -> list:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_skipped_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_skipped_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueHistorySkippedEntries:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_skipped_entry

    out: BatchGetAssetPropertyValueHistorySkippedEntries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_skipped_entry.deserialize_json(
                item
            )
        )
    return out
