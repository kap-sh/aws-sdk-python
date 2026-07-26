"""Generated from Smithy shape ``com.amazonaws.mgn#VcenterClientList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.vcenter_client

VcenterClientList: TypeAlias = list["capo_mgn.types.vcenter_client.VcenterClient"]


# --- restJson1 ser/de ---
def serialize_json(value: VcenterClientList) -> list:
    import capo_mgn.types.vcenter_client

    out: list = []
    for item in value:
        out.append(capo_mgn.types.vcenter_client.serialize_json(item))
    return out


def deserialize_json(data: list) -> VcenterClientList:
    import capo_mgn.types.vcenter_client

    out: VcenterClientList = []
    for item in data:
        out.append(capo_mgn.types.vcenter_client.deserialize_json(item))
    return out
