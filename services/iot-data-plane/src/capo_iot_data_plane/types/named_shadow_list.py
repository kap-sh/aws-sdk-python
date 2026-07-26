"""Generated from Smithy shape ``com.amazonaws.iotdataplane#NamedShadowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_data_plane.types.shadow_name

NamedShadowList: TypeAlias = list["capo_iot_data_plane.types.shadow_name.ShadowName"]


# --- restJson1 ser/de ---
def serialize_json(value: NamedShadowList) -> list:
    return list(value)


def deserialize_json(data: list) -> NamedShadowList:
    return list(data)
