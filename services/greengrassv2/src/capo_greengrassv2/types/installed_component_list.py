"""Generated from Smithy shape ``com.amazonaws.greengrassv2#InstalledComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.installed_component

InstalledComponentList: TypeAlias = list[
    "capo_greengrassv2.types.installed_component.InstalledComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstalledComponentList) -> list:
    import capo_greengrassv2.types.installed_component

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.installed_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> InstalledComponentList:
    import capo_greengrassv2.types.installed_component

    out: InstalledComponentList = []
    for item in data:
        out.append(capo_greengrassv2.types.installed_component.deserialize_json(item))
    return out
