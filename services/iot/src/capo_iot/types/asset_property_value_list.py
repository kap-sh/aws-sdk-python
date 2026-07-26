"""Generated from Smithy shape ``com.amazonaws.iot#AssetPropertyValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.asset_property_value

AssetPropertyValueList: TypeAlias = list[
    "capo_iot.types.asset_property_value.AssetPropertyValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyValueList) -> list:
    import capo_iot.types.asset_property_value

    out: list = []
    for item in value:
        out.append(capo_iot.types.asset_property_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetPropertyValueList:
    import capo_iot.types.asset_property_value

    out: AssetPropertyValueList = []
    for item in data:
        out.append(capo_iot.types.asset_property_value.deserialize_json(item))
    return out
