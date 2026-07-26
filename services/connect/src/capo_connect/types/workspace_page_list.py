"""Generated from Smithy shape ``com.amazonaws.connect#WorkspacePageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.workspace_page

WorkspacePageList: TypeAlias = list["capo_connect.types.workspace_page.WorkspacePage"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspacePageList) -> list:
    import capo_connect.types.workspace_page

    out: list = []
    for item in value:
        out.append(capo_connect.types.workspace_page.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkspacePageList:
    import capo_connect.types.workspace_page

    out: WorkspacePageList = []
    for item in data:
        out.append(capo_connect.types.workspace_page.deserialize_json(item))
    return out
