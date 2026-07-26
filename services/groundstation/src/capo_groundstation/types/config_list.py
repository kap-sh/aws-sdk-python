"""Generated from Smithy shape ``com.amazonaws.groundstation#ConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.config_list_item

ConfigList: TypeAlias = list["capo_groundstation.types.config_list_item.ConfigListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigList) -> list:
    import capo_groundstation.types.config_list_item

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.config_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfigList:
    import capo_groundstation.types.config_list_item

    out: ConfigList = []
    for item in data:
        out.append(capo_groundstation.types.config_list_item.deserialize_json(item))
    return out
