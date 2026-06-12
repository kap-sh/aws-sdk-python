"""Generated from Smithy shape ``com.amazonaws.workspacesweb#BlockedCategories``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.category

BlockedCategories: TypeAlias = list["aws_sdk_workspaces_web.types.category.Category"]


# --- restJson1 ser/de ---
def serialize_json(value: BlockedCategories) -> list:
    import aws_sdk_workspaces_web.types.category
    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_web.types.category.serialize_json(item))
    return out


def deserialize_json(data: list) -> BlockedCategories:
    import aws_sdk_workspaces_web.types.category
    out: BlockedCategories = []
    for item in data:
        out.append(aws_sdk_workspaces_web.types.category.deserialize_json(item))
    return out