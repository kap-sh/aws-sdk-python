"""Generated from Smithy shape ``com.amazonaws.iot#PutAssetPropertyValueEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.put_asset_property_value_entry

PutAssetPropertyValueEntryList: TypeAlias = list[
    "capo_iot.types.put_asset_property_value_entry.PutAssetPropertyValueEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: PutAssetPropertyValueEntryList) -> list:
    import capo_iot.types.put_asset_property_value_entry

    out: list = []
    for item in value:
        out.append(capo_iot.types.put_asset_property_value_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> PutAssetPropertyValueEntryList:
    import capo_iot.types.put_asset_property_value_entry

    out: PutAssetPropertyValueEntryList = []
    for item in data:
        out.append(capo_iot.types.put_asset_property_value_entry.deserialize_json(item))
    return out
