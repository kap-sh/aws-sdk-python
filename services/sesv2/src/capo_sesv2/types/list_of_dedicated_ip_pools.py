"""Generated from Smithy shape ``com.amazonaws.sesv2#ListOfDedicatedIpPools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.pool_name

ListOfDedicatedIpPools: TypeAlias = list["capo_sesv2.types.pool_name.PoolName"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDedicatedIpPools) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfDedicatedIpPools:
    return list(data)
