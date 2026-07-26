"""Generated from Smithy shape ``com.amazonaws.outposts#HostIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.host_id

HostIdList: TypeAlias = list["capo_outposts.types.host_id.HostId"]


# --- restJson1 ser/de ---
def serialize_json(value: HostIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> HostIdList:
    return list(data)
