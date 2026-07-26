"""Generated from Smithy shape ``com.amazonaws.appintegrations#IframePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appintegrations.types.iframe_permission

IframePermissionList: TypeAlias = list[
    "capo_appintegrations.types.iframe_permission.IframePermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: IframePermissionList) -> list:
    return list(value)


def deserialize_json(data: list) -> IframePermissionList:
    return list(data)
