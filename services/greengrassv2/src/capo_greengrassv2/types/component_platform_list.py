"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentPlatformList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_platform

ComponentPlatformList: TypeAlias = list[
    "capo_greengrassv2.types.component_platform.ComponentPlatform"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentPlatformList) -> list:
    import capo_greengrassv2.types.component_platform

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.component_platform.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentPlatformList:
    import capo_greengrassv2.types.component_platform

    out: ComponentPlatformList = []
    for item in data:
        out.append(capo_greengrassv2.types.component_platform.deserialize_json(item))
    return out
