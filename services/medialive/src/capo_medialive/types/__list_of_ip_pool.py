"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfIpPool``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.ip_pool

__listOfIpPool: TypeAlias = list["capo_medialive.types.ip_pool.IpPool"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfIpPool) -> list:
    import capo_medialive.types.ip_pool

    out: list = []
    for item in value:
        out.append(capo_medialive.types.ip_pool.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfIpPool:
    import capo_medialive.types.ip_pool

    out: __listOfIpPool = []
    for item in data:
        out.append(capo_medialive.types.ip_pool.deserialize_json(item))
    return out
