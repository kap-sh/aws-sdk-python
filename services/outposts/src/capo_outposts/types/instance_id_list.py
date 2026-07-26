"""Generated from Smithy shape ``com.amazonaws.outposts#InstanceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.instance_id

InstanceIdList: TypeAlias = list["capo_outposts.types.instance_id.InstanceId"]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceIdList:
    return list(data)
