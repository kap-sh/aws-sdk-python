"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentConfigurationPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_configuration_path

ComponentConfigurationPathList: TypeAlias = list[
    "capo_greengrassv2.types.component_configuration_path.ComponentConfigurationPath"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConfigurationPathList) -> list:
    return list(value)


def deserialize_json(data: list) -> ComponentConfigurationPathList:
    return list(data)
