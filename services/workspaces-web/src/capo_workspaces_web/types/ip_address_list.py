"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.ip_address

IpAddressList: TypeAlias = list["capo_workspaces_web.types.ip_address.IpAddress"]


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> IpAddressList:
    return list(data)
