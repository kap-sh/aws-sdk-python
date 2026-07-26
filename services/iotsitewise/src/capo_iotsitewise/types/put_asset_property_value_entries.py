"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutAssetPropertyValueEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.put_asset_property_value_entry

PutAssetPropertyValueEntries: TypeAlias = list[
    "capo_iotsitewise.types.put_asset_property_value_entry.PutAssetPropertyValueEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: PutAssetPropertyValueEntries) -> list:
    import capo_iotsitewise.types.put_asset_property_value_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.put_asset_property_value_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PutAssetPropertyValueEntries:
    import capo_iotsitewise.types.put_asset_property_value_entry

    out: PutAssetPropertyValueEntries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.put_asset_property_value_entry.deserialize_json(item)
        )
    return out
