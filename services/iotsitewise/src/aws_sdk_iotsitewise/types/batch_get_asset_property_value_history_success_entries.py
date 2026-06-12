"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistorySuccessEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_success_entry

BatchGetAssetPropertyValueHistorySuccessEntries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_success_entry.BatchGetAssetPropertyValueHistorySuccessEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistorySuccessEntries) -> list:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_success_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_success_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueHistorySuccessEntries:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_success_entry

    out: BatchGetAssetPropertyValueHistorySuccessEntries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_success_entry.deserialize_json(
                item
            )
        )
    return out
