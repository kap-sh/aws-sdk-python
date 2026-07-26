"""Generated from Smithy shape ``com.amazonaws.sesv2#ConfigurationSetNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name

ConfigurationSetNameList: TypeAlias = list[
    "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationSetNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConfigurationSetNameList:
    return list(data)
