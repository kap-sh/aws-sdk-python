"""Generated from Smithy shape ``com.amazonaws.workspacesweb#HiddenToolbarItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.toolbar_item

HiddenToolbarItemList: TypeAlias = list[
    "capo_workspaces_web.types.toolbar_item.ToolbarItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: HiddenToolbarItemList) -> list:
    return list(value)


def deserialize_json(data: list) -> HiddenToolbarItemList:
    return list(data)
