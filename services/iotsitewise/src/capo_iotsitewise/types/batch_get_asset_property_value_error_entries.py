"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_value_error_entry

BatchGetAssetPropertyValueErrorEntries: TypeAlias = list[
    "capo_iotsitewise.types.batch_get_asset_property_value_error_entry.BatchGetAssetPropertyValueErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueErrorEntries) -> list:
    import capo_iotsitewise.types.batch_get_asset_property_value_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetAssetPropertyValueErrorEntries:
    import capo_iotsitewise.types.batch_get_asset_property_value_error_entry

    out: BatchGetAssetPropertyValueErrorEntries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.batch_get_asset_property_value_error_entry.deserialize_json(
                item
            )
        )
    return out
