"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.software

SoftwareList: TypeAlias = list["capo_workspaces_thin_client.types.software.Software"]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareList) -> list:
    import capo_workspaces_thin_client.types.software

    out: list = []
    for item in value:
        out.append(capo_workspaces_thin_client.types.software.serialize_json(item))
    return out


def deserialize_json(data: list) -> SoftwareList:
    import capo_workspaces_thin_client.types.software

    out: SoftwareList = []
    for item in data:
        out.append(capo_workspaces_thin_client.types.software.deserialize_json(item))
    return out
