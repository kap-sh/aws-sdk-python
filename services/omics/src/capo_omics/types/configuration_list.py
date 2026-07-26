"""Generated from Smithy shape ``com.amazonaws.omics#ConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.configuration_list_item

ConfigurationList: TypeAlias = list[
    "capo_omics.types.configuration_list_item.ConfigurationListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationList) -> list:
    import capo_omics.types.configuration_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.configuration_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfigurationList:
    import capo_omics.types.configuration_list_item

    out: ConfigurationList = []
    for item in data:
        out.append(capo_omics.types.configuration_list_item.deserialize_json(item))
    return out
