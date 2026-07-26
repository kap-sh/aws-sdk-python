"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_version_list_item

ComponentVersionList: TypeAlias = list[
    "capo_greengrassv2.types.component_version_list_item.ComponentVersionListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVersionList) -> list:
    import capo_greengrassv2.types.component_version_list_item

    out: list = []
    for item in value:
        out.append(
            capo_greengrassv2.types.component_version_list_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComponentVersionList:
    import capo_greengrassv2.types.component_version_list_item

    out: ComponentVersionList = []
    for item in data:
        out.append(
            capo_greengrassv2.types.component_version_list_item.deserialize_json(item)
        )
    return out
