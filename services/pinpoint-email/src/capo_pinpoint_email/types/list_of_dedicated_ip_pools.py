"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListOfDedicatedIpPools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.pool_name

ListOfDedicatedIpPools: TypeAlias = list["capo_pinpoint_email.types.pool_name.PoolName"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDedicatedIpPools) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfDedicatedIpPools:
    return list(data)
