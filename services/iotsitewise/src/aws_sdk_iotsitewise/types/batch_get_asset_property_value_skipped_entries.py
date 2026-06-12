"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueSkippedEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entry

BatchGetAssetPropertyValueSkippedEntries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entry.BatchGetAssetPropertyValueSkippedEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueSkippedEntries) -> list:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueSkippedEntries:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entry

    out: BatchGetAssetPropertyValueSkippedEntries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entry.deserialize_json(
                item
            )
        )
    return out
