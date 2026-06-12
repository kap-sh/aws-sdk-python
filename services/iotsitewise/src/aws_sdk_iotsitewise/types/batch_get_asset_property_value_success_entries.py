"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueSuccessEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entry

BatchGetAssetPropertyValueSuccessEntries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entry.BatchGetAssetPropertyValueSuccessEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueSuccessEntries) -> list:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueSuccessEntries:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entry

    out: BatchGetAssetPropertyValueSuccessEntries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entry.deserialize_json(
                item
            )
        )
    return out
